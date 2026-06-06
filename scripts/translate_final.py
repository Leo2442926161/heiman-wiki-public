#!/usr/bin/env python3
"""Parallel batch translation with aggressive retry and error handling."""

import json, os, re, sys, time, urllib.parse, urllib.request, ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
I18N_DIR = BASE_DIR / "i18n"
LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]
PROXY = "http://127.0.0.1:11000"
CN_PATTERN = re.compile(r'[\u4e00-\u9fff]')
HIRAGANA = re.compile(r'[\u3040-\u309f]')
KATAKANA = re.compile(r'[\u30a0-\u30ff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')
PRESERVE = {"海曼": "Heiman", "海曼科技": "Heiman Technology"}
MAX_WORKERS = 4

print_lock = Lock()
stats_lock = Lock()

def log(msg):
    with print_lock:
        print(msg, flush=True)

def has_chinese(text, locale=None):
    if not text.strip():
        return False
    if locale == "ja":
        # Japanese should have hiragana or katakana if translated
        if HIRAGANA.search(text) or KATAKANA.search(text):
            return False  # Has Japanese script = translated
        return bool(CN_PATTERN.search(text))  # Only CJK chars = still Chinese
    if locale == "ko":
        # Korean should have hangul if translated
        if HANGUL.search(text):
            return False  # Has Hangul = translated
        return bool(CN_PATTERN.search(text))  # Only CJK chars = still Chinese
    # Other locales: any CJK means untranslated Chinese
    return bool(CN_PATTERN.search(text))

def translate_text(text, target):
    if not text.strip():
        return text
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": "zh-CN", "tl": target, "dt": "t", "q": text}
    full_url = url + "?" + urllib.parse.urlencode(params)
    for attempt in range(10):
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(full_url, headers={
                "User-Agent": "Mozilla/5.0"
            })
            ph = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
            opener = urllib.request.build_opener(ph)
            with opener.open(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                result = "".join(p[0] for p in data[0])
            for ch, en in PRESERVE.items():
                result = result.replace(ch, en)
            if has_chinese(result, target):
                time.sleep(2)
                continue
            return result
        except Exception:
            if attempt < 9:
                time.sleep(1.5)
                continue
    return None

def process_file(args):
    src_path, target_dir, locale = args
    rel = src_path.relative_to(DOCS_DIR)
    target_path = target_dir / rel

    # Check if already translated
    if target_path.exists():
        try:
            c = target_path.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n.*?\n---\s*\n", c, re.DOTALL)
            b = c[m.end():] if m else c
            if not has_chinese(b, locale):
                return ("skip", rel)
        except:
            pass

    try:
        content = src_path.read_text(encoding="utf-8")
    except Exception:
        return ("fail", rel)

    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if m:
        fm_text, body = m.group(1), content[m.end():]
    else:
        fm_text, body = "", content

    # Translate title
    if fm_text:
        try:
            fm = {}
            for line in fm_text.split("\n"):
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip()
            if "title" in fm and fm["title"] and has_chinese(fm["title"], locale):
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
        except:
            pass

    # Translate body
    if body.strip() and has_chinese(body, locale):
        if len(body) > 3000:
            chunks = []
            for pos in range(0, len(body), 3000):
                chunk = body[pos:pos + 3000]
                tr = translate_text(chunk, locale)
                chunks.append(tr if tr else chunk)
                time.sleep(0.3)
            tbody = "".join(chunks)
        else:
            tbody = translate_text(body, locale)
        if tbody:
            body = tbody

    result = f"---\n{fm_text}\n---\n{body}" if fm_text else body
    body_check = re.sub(r'---\s*\n.*?\n---\s*\n', '', result, flags=re.DOTALL) if fm_text else result

    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(result, encoding="utf-8")
    except Exception:
        return ("fail", rel)

    if has_chinese(body_check, locale):
        return ("fail", rel)
    return ("ok", rel)

def process_locale(locale):
    src_files = sorted(DOCS_DIR.rglob("*.md"))
    target_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"
    total = len(src_files)

    log(f"\n[{locale}] Starting {total} files ({MAX_WORKERS} workers)...")

    args_list = [(s, target_dir, locale) for s in src_files]
    stats = {"ok": 0, "fail": 0, "skip": 0}
    done = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(process_file, a): a[0] for a in args_list}
        for f in as_completed(futures):
            done += 1
            result, rel = f.result()
            stats[result] += 1
            if done % 15 == 0 or done == total:
                log(f"  [{locale}] {done}/{total} ok={stats['ok']} fail={stats['fail']} skip={stats['skip']}")

    log(f"[{locale}] DONE: ok={stats['ok']} fail={stats['fail']} skip={stats['skip']}")
    return stats

if __name__ == "__main__":
    total_ok = total_fail = 0
    for loc in LOCALES:
        s = process_locale(loc)
        total_ok += s["ok"]
        total_fail += s["fail"]
        time.sleep(3)
    log(f"\nGRAND TOTAL: {total_ok} OK, {total_fail} FAIL")
