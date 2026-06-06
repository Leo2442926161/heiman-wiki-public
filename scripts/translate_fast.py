#!/usr/bin/env python3
"""Fast batch translation via Google Translate API with parallel workers."""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
I18N_DIR = BASE_DIR / "i18n"
LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]
PROXY = "http://127.0.0.1:11000"
MAX_WORKERS = 6

print_lock = Lock()
stats_lock = Lock()
stats = {"ok": 0, "fail": 0, "skip": 0}

# Brand names and terms to preserve (Chinese → original)
PRESERVE = {
    "海曼": "Heiman",
    "海曼科技": "Heiman Technology",
}

def log(msg):
    with print_lock:
        print(msg, file=sys.stderr, flush=True)

def translate_text(text, target):
    """Translate via Google Translate API using urllib + proxy."""
    if not text.strip():
        return text

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "zh-CN",
        "tl": target,
        "dt": "t",
        "q": text,
    }
    full_url = url + "?" + urllib.parse.urlencode(params)

    for attempt in range(3):
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(full_url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            })
            proxy_handler = urllib.request.ProxyHandler({
                "http": PROXY,
                "https": PROXY,
            })
            opener = urllib.request.build_opener(proxy_handler)
            with opener.open(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                result = "".join(part[0] for part in data[0])
            # Restore brand names
            for ch, en in PRESERVE.items():
                result = result.replace(ch, en)
            # Restore URLs (sometimes Google Translate mangles them)
            url_pattern = re.compile(r'https?://[^\s）\)。，,;；》">]+')
            original_urls = url_pattern.findall(text)
            translated_urls = url_pattern.findall(result)
            for ou, tu in zip(original_urls, translated_urls):
                if ou != tu and tu in result:
                    result = result.replace(tu, ou)
            return result
        except Exception:
            if attempt < 2:
                time.sleep(1)
                continue
            return None
    return None


def split_frontmatter(content):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if m:
        return m.group(1), content[m.end():]
    return "", content


def parse_fm(text):
    fm = {}
    for line in text.split("\n"):
        line = line.rstrip()
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm


def rebuild_fm(parsed, original_text):
    lines = original_text.split("\n")
    result = []
    for line in lines:
        if ":" in line:
            key, _, val = line.partition(":")
            k = key.strip()
            if k in parsed:
                indent = line[:len(line) - len(line.lstrip())]
                result.append(f"{indent}{k}: {parsed[k]}")
                continue
        result.append(line)
    return "\n".join(result)


def translate_file(src_path, locale):
    rel = src_path.relative_to(DOCS_DIR)
    target_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"
    target_path = target_dir / rel

    if target_path.exists():
        with stats_lock:
            stats["skip"] += 1
        return

    content = src_path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(content)

    # Translate frontmatter title
    if fm_text:
        fm = parse_fm(fm_text)
        if "title" in fm and fm["title"]:
            t = translate_text(fm["title"], locale)
            if t:
                fm["title"] = t
        fm_text = rebuild_fm(fm, fm_text)

    # Translate body
    if body.strip():
        max_chunk = 4000
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

    result = f"---\n{fm_text}\n---\n{body}" if fm_text else body
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(result, encoding="utf-8")

    with stats_lock:
        stats["ok"] += 1


def translate_locale(locale):
    src_files = sorted(DOCS_DIR.rglob("*.md"))
    total = len(src_files)
    log(f"[{locale}] Translating {total} files ({MAX_WORKERS} workers)...")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = [ex.submit(translate_file, src, locale) for src in src_files]
        done = 0
        for f in as_completed(futures):
            done += 1
            if done % 20 == 0 or done == total:
                with stats_lock:
                    log(f"[{locale}] {done}/{total} (ok={stats['ok']} fail={stats['fail']} skip={stats['skip']})")
            try:
                f.result()
            except Exception:
                with stats_lock:
                    stats["fail"] += 1

    with stats_lock:
        log(f"[{locale}] DONE: {stats['ok']} translated, {stats['fail']} failed, {stats['skip']} skipped")
        stats["ok"] = 0
        stats["fail"] = 0
        stats["skip"] = 0


if __name__ == "__main__":
    log(f"Starting translation for {len(LOCALES)} locales...")
    for loc in LOCALES:
        translate_locale(loc)
        time.sleep(2)
    log("ALL DONE!")
