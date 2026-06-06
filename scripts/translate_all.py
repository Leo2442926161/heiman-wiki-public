#!/usr/bin/env python3
"""Batch translate all Chinese .md docs to all non-zh locales via Google Translate API."""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import ssl
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
I18N_DIR = BASE_DIR / "i18n"

LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]

PROXY = "http://127.0.0.1:11000"

# Track rate limiting
last_call = 0
MIN_INTERVAL = 0.3  # seconds between calls


def translate_text(text, source="zh-CN", target="de"):
    """Translate text using Google Translate API via proxy."""
    global last_call

    if not text.strip():
        return text

    # Rate limit
    elapsed = time.time() - last_call
    if elapsed < MIN_INTERVAL:
        time.sleep(MIN_INTERVAL - elapsed)

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": source,
        "tl": target,
        "dt": "t",
        "q": text,
    }
    full_url = url + "?" + urllib.parse.urlencode(params)

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
        resp = opener.open(req, timeout=15)
        data = json.loads(resp.read().decode())
        result = "".join(part[0] for part in data[0])
        last_call = time.time()
        return result
    except Exception as e:
        print(f"  [WARN] Translation failed: {e}", file=sys.stderr)
        return None


def split_frontmatter(content):
    """Split markdown content into (frontmatter_dict, body)."""
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        body = content[fm_match.end():]
        # Parse frontmatter
        fm = {}
        current_key = None
        for line in fm_text.split("\n"):
            line = line.rstrip()
            if not line:
                continue
            if line[0].isspace() and current_key:
                # Continuation of previous value
                fm[current_key] = fm[current_key].strip() + "\n" + line.strip()
            elif ":" in line:
                key, _, val = line.partition(":")
                current_key = key.strip()
                fm[current_key] = val.strip()
            else:
                current_key = None
        return fm, body, fm_text
    return {}, content, ""


def reconstruct_frontmatter(fm, original_fm_text):
    """Reconstruct frontmatter text from dict using original as template for formatting."""
    lines = original_fm_text.split("\n")
    new_lines = []
    for line in lines:
        if ":" in line:
            key, _, val = line.partition(":")
            k = key.strip()
            if k in fm:
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append(f"{indent}{k}: {fm[k]}")
                continue
        new_lines.append(line)
    return "\n".join(new_lines)


def translate_file(src_path, target_locale, target_path):
    """Translate a single .md file and write to target path."""
    content = src_path.read_text(encoding="utf-8")

    fm, body, fm_text = split_frontmatter(content)

    # Translate frontmatter title if present
    if "title" in fm and fm["title"]:
        translated_title = translate_text(fm["title"], target=target_locale)
        if translated_title:
            fm["title"] = translated_title

    # Translate the body
    if body.strip():
        translated_body = translate_text(body, target=target_locale)
        if translated_body:
            body = translated_body
    else:
        translated_body = body

    # Reconstruct
    if fm:
        new_fm_text = reconstruct_frontmatter(fm, fm_text)
        result = f"---\n{new_fm_text}\n---\n{body}"
    else:
        result = body

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(result, encoding="utf-8")
    return True


def main():
    # Collect all source .md files
    src_files = sorted(DOCS_DIR.rglob("*.md"))
    total = len(src_files)
    print(f"Found {total} source .md files to translate", file=sys.stderr)

    for locale in LOCALES:
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"Translating to: {locale} ({LOCALES.index(locale)+1}/{len(LOCALES)})", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)

        locale_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"
        locale_dir.mkdir(parents=True, exist_ok=True)

        success = 0
        fail = 0
        skip = 0

        for i, src_path in enumerate(src_files):
            rel_path = src_path.relative_to(DOCS_DIR)
            target_path = locale_dir / rel_path

            if target_path.exists():
                skip += 1
                if i % 20 == 0:
                    print(f"  [{i+1}/{total}] SKIP {rel_path} (exists)", file=sys.stderr)
                continue

            print(f"  [{i+1}/{total}] {rel_path}", file=sys.stderr)

            # Translate in chunks for large files
            content = src_path.read_text(encoding="utf-8")
            fm, body, fm_text = split_frontmatter(content)

            # Translate title
            translated_title = None
            if "title" in fm and fm["title"]:
                translated_title = translate_text(fm["title"], target=locale)
                if translated_title:
                    fm["title"] = translated_title

            # Translate body in chunks if > 4000 chars
            if body.strip():
                max_chunk = 3000
                if len(body) > max_chunk:
                    chunked_result = []
                    pos = 0
                    while pos < len(body):
                        chunk = body[pos:pos + max_chunk]
                        tr = translate_text(chunk, target=locale)
                        if tr:
                            chunked_result.append(tr)
                        else:
                            chunked_result.append(chunk)
                        pos += max_chunk
                    translated_body = "".join(chunked_result)
                else:
                    translated_body = translate_text(body, target=locale)

                if translated_body:
                    body = translated_body

            # Write result
            if fm:
                new_fm_text = reconstruct_frontmatter(fm, fm_text)
                result = f"---\n{new_fm_text}\n---\n{body}"
            else:
                result = body

            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(result, encoding="utf-8")
            success += 1

            if (i + 1) % 10 == 0:
                print(f"  --- Progress: {i+1}/{total} ({success} OK, {fail} fail, {skip} skip)", file=sys.stderr)

        print(f"  Locale {locale}: {success} translated, {fail} failed, {skip} skipped", file=sys.stderr)

    print(f"\n{'='*60}", file=sys.stderr)
    print("Done!", file=sys.stderr)


if __name__ == "__main__":
    main()
