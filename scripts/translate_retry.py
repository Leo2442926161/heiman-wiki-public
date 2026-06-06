#!/usr/bin/env python3
"""Retry translation for files still in Chinese, with validation."""

import json, os, re, sys, time, urllib.parse, urllib.request, ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
I18N_DIR = BASE_DIR / "i18n"
LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]
PROXY = "http://127.0.0.1:11000"
MAX_WORKERS = 3  # fewer workers to avoid rate limiting

cn_pattern = re.compile(r'[\u4e00-\u9fff]')
print_lock = Lock()
stats_lock = Lock()
global_stats = {"ok": 0, "fail": 0}

PRESERVE = {"海曼": "Heiman", "海曼科技": "Heiman Technology"}

def log(msg):
    with print_lock:
        print(msg, file=sys.stderr, flush=True)

def has_chinese(text):
    return bool(cn_pattern.search(text))

def translate_text(text, target):
    if not text.strip():
        return text
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": "zh-CN", "tl": target, "dt": "t", "q": text}
    full_url = url + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(full_url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            })
            ph = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
            opener = urllib.request.build_opener(ph)
            with opener.open(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                result = "".join(part[0] for part in data[0])
            for ch, en in PRESERVE.items():
                result = result.replace(ch, en)
            # Check if result still has Chinese
            if has_chinese(result):
                log(f"    Retry {attempt+1}: result still has Chinese chars")
                time.sleep(2)
                continue
            return result
        except Exception as e:
            log(f"    Attempt {attempt+1} failed: {e}")
            if attempt < 4:
                time.sleep(2.5)
                continue
    return None

def translate_file(src_path, locale):
    rel = src_path.relative_to(DOCS_DIR)
    target_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"
    target_path = target_dir / rel

    content = src_path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if m:
        fm_text, body = m.group(1), content[m.end():]
    else:
        fm_text, body = "", content

    # Translate title in frontmatter
    if fm_text:
        fm = {}
        for line in fm_text.split("\n"):
            if ":" in line:
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()
        if "title" in fm and fm["title"] and has_chinese(fm["title"]):
            t = translate_text(fm["title"], locale)
            if t:
                fm["title"] = t
        # Rebuild
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
    if body.strip() and has_chinese(body):
        max_chunk = 3000
        if len(body) > max_chunk:
            chunks = []
            pos = 0
            while pos < len(body):
                chunk = body[pos:pos + max_chunk]
                tr = translate_text(chunk, locale)
                chunks.append(tr if tr else chunk)
                pos += max_chunk
            tbody = "".join(chunks)
        else:
            tbody = translate_text(body, locale)
        if tbody:
            body = tbody

    # Final Chinese check
    result = f"---\n{fm_text}\n---\n{body}" if fm_text else body
    if has_chinese(re.sub(r'---\s*\n.*?\n---\s*\n', '', result, flags=re.DOTALL) if fm_text else result):
        with stats_lock:
            global_stats["fail"] += 1
        log(f"  FAILED after retries: {rel}")
        return False

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(result, encoding="utf-8")
    with stats_lock:
        global_stats["ok"] += 1
    return True


def process_locale(locale):
    global global_stats
    global_stats = {"ok": 0, "fail": 0}

    src_files = sorted(DOCS_DIR.rglob("*.md"))
    target_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"

    # Find files still in Chinese
    todo = []
    for src in src_files:
        rel = src.relative_to(DOCS_DIR)
        tgt = target_dir / rel
        if not tgt.exists():
            todo.append((src, True))  # missing
        else:
            content = tgt.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n.*?\n---\s*\n", content, re.DOTALL)
            body = content[m.end():] if m else content
            if has_chinese(body):
                todo.append((src, False))  # needs retranslation

    total = len(todo)
    if total == 0:
        log(f"[{locale}] All {len(src_files)} files already translated. SKIP.")
        return

    log(f"[{locale}] {total} files need translation ({len(src_files)} total)...")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(translate_file, src, locale): src for src, _ in todo}
        done = 0
        for f in as_completed(futures):
            done += 1
            if done % 10 == 0 or done == total:
                with stats_lock:
                    log(f"[{locale}] {done}/{total} (ok={global_stats['ok']} fail={global_stats['fail']})")

    log(f"[{locale}] DONE: {global_stats['ok']} translated, {global_stats['fail']} failed")


if __name__ == "__main__":
    log(f"Retry translation for remaining Chinese content...")
    for loc in LOCALES:
        process_locale(loc)
        time.sleep(3)
    log("ALL DONE!")
