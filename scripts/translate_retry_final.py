#!/usr/bin/env python3
"""Retry translation for files still containing Chinese text."""

import json, os, re, sys, time, urllib.request, urllib.parse, ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
I18N_DIR = BASE_DIR / "i18n"
LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]
PROXY = "http://127.0.0.1:11000"
CN = re.compile(r'[\u4e00-\u9fff]')
HI = re.compile(r'[\u3040-\u309f]')
KA = re.compile(r'[\u30a0-\u30ff]')
HA = re.compile(r'[\uac00-\ud7af]')
PRESERVE = {"海曼": "Heiman", "海曼科技": "Heiman Technology"}
MAX_WORKERS = 3
print_lock = Lock()

def log(msg):
    with print_lock:
        print(msg, flush=True)

def still_chinese(text, locale):
    if not text.strip():
        return False
    if locale == "ja":
        if HI.search(text) or KA.search(text):
            return False
        return bool(CN.search(text))
    if locale == "ko":
        if HA.search(text):
            return False
        return bool(CN.search(text))
    return bool(CN.search(text))

def translate_text(text, target):
    if not text.strip():
        return text
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": "zh-CN", "tl": target, "dt": "t", "q": text}
    full_url = url + "?" + urllib.parse.urlencode(params)
    for attempt in range(12):
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(full_url, headers={"User-Agent": "Mozilla/5.0"})
            ph = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
            opener = urllib.request.build_opener(ph)
            with opener.open(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                result = "".join(p[0] for p in data[0])
            for ch, en in PRESERVE.items():
                result = result.replace(ch, en)
            if still_chinese(result, target):
                time.sleep(3)
                continue
            return result
        except Exception:
            if attempt < 11:
                time.sleep(2)
                continue
    return None

def retry_file(args):
    src_path, target_dir, locale = args
    rel = src_path.relative_to(DOCS_DIR)
    target_path = target_dir / rel

    if not target_path.exists():
        return ("skip", rel)

    try:
        content = target_path.read_text(encoding="utf-8")
    except:
        return ("skip", rel)

    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    body = content[m.end():] if m else content

    if not still_chinese(body, locale):
        return ("skip", rel)

    # Read source and retranslate
    try:
        src_content = src_path.read_text(encoding="utf-8")
    except:
        return ("fail", rel)

    m2 = re.match(r"^---\s*\n(.*?)\n---\s*\n", src_content, re.DOTALL)
    if m2:
        fm_text, body = m2.group(1), src_content[m2.end():]
    else:
        fm_text, body = "", src_content

    # Translate title
    if fm_text:
        fm = {}
        for line in fm_text.split("\n"):
            if ":" in line:
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()
        if "title" in fm and fm["title"] and still_chinese(fm["title"], locale):
            t = translate_text(fm["title"], locale)
            if t:
                fm["title"] = t
        new_lines = []
        for line in fm_text.split("\n"):
            if ":" in line:
                k = line.partition(":")[0].strip()
                if k in fm:
                    indent = line[:len(line) - len(line.lstrip())]
                    new_lines.append(f"{indent}{k}: {fm[k]}")
                    continue
            new_lines.append(line)
        fm_text = "\n".join(new_lines)

    # Translate body
    if body.strip() and still_chinese(body, locale):
        if len(body) > 3000:
            chunks = []
            for pos in range(0, len(body), 3000):
                chunk = body[pos:pos + 3000]
                tr = translate_text(chunk, locale)
                chunks.append(tr if tr else chunk)
                time.sleep(0.5)
            tbody = "".join(chunks)
        else:
            tbody = translate_text(body, locale)
        if tbody:
            body = tbody

    result = f"---\n{fm_text}\n---\n{body}" if fm_text else body
    try:
        target_path.write_text(result, encoding="utf-8")
    except:
        return ("fail", rel)

    body_check = re.sub(r'---\s*\n.*?\n---\s*\n', '', result, flags=re.DOTALL) if fm_text else result
    if still_chinese(body_check, locale):
        return ("fail", rel)
    return ("ok", rel)


if __name__ == "__main__":
    for locale in LOCALES:
        src_files = sorted(DOCS_DIR.rglob("*.md"))
        target_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"
        args_list = [(s, target_dir, locale) for s in src_files]

        log(f"\n[{locale}] Retrying...")
        ok = fail = skip = 0
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
            futures = {ex.submit(retry_file, a): a[0] for a in args_list}
            for f in as_completed(futures):
                r, _ = f.result()
                if r == "ok": ok += 1
                elif r == "fail": fail += 1
                else: skip += 1

        log(f"[{locale}] ok={ok} fail={fail} skip={skip}")
        time.sleep(2)

    # Final count
    log("\n=== FINAL CHECK ===")
    cn_total = 0
    for loc in LOCALES:
        base = f"i18n/{loc}/docusaurus-plugin-content-docs/current/docs"
        c = 0
        t = 0
        for root, dirs, files in os.walk(base):
            for f in files:
                if not f.endswith('.md'): continue
                t += 1
                content = open(os.path.join(root, f), encoding='utf-8').read()
                m = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
                body = content[m.end():] if m else content
                if still_chinese(body, loc):
                    c += 1
        cn_total += c
        log(f"  {loc}: {t} files, {c} Chinese")
    log(f"\nTOTAL Chinese files remaining: {cn_total}")
