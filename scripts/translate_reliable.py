#!/usr/bin/env python3
"""Reliable sequential translation via Google Translate using requests Session."""

import json, os, re, sys, time, hashlib
from pathlib import Path
import requests
import urllib3
urllib3.disable_warnings()

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
I18N_DIR = BASE_DIR / "i18n"
LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]
PROXY = "http://127.0.0.1:11000"

# Preserve brand names
PRESERVE = {"海曼": "Heiman", "海曼科技": "Heiman Technology"}
CN_PATTERN = re.compile(r'[\u4e00-\u9fff]')

def has_chinese(text):
    return bool(CN_PATTERN.search(text))

def translate_text(text, target, session):
    if not text.strip():
        return text
    for attempt in range(5):
        try:
            resp = session.get(
                "https://translate.googleapis.com/translate_a/single",
                params={"client": "gtx", "sl": "zh-CN", "tl": target, "dt": "t", "q": text},
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=30
            )
            data = resp.json()
            result = "".join(p[0] for p in data[0])
            for ch, en in PRESERVE.items():
                result = result.replace(ch, en)
            if has_chinese(result):
                time.sleep(2 * (attempt + 1))
                continue
            return result
        except Exception as e:
            if attempt < 4:
                time.sleep(3 * (attempt + 1))
                continue
    return None

def process_locale(locale):
    print(f"\n[{locale}] Starting...", flush=True)

    # Create session with explicit proxy
    session = requests.Session()
    session.trust_env = False
    session.verify = False
    session.proxies = {"http": PROXY, "https": PROXY}

    # Warm up the proxy connection
    for _ in range(3):
        try:
            session.get("https://translate.googleapis.com/translate_a/single",
                       params={"client": "gtx", "sl": "en", "tl": "de", "dt": "t", "q": "hello"},
                       timeout=15)
            break
        except Exception:
            time.sleep(2)

    src_files = sorted(DOCS_DIR.rglob("*.md"))
    target_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"
    total = len(src_files)
    ok = fail = skip = 0

    for i, src_path in enumerate(src_files):
        rel = src_path.relative_to(DOCS_DIR)
        target_path = target_dir / rel

        if target_path.exists() and not has_chinese(target_path.read_text(encoding="utf-8")):
            skip += 1
            if (i + 1) % 20 == 0 or i == 0:
                print(f"  [{i+1}/{total}] SKIP {rel}", flush=True)
            continue

        content = src_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if m:
            fm_text, body = m.group(1), content[m.end():]
        else:
            fm_text, body = "", content

        if (i + 1) % 5 == 0 or i == 0:
            print(f"  [{i+1}/{total}] {rel}...", flush=True)

        # Translate title
        if fm_text:
            fm = {}
            for line in fm_text.split("\n"):
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip()
            if "title" in fm and fm["title"] and has_chinese(fm["title"]):
                t = translate_text(fm["title"], locale, session)
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
        if body.strip() and has_chinese(body):
            max_chunk = 2500
            if len(body) > max_chunk:
                chunks = []
                pos = 0
                while pos < len(body):
                    chunk = body[pos:pos + max_chunk]
                    tr = translate_text(chunk, locale, session)
                    chunks.append(tr if tr else chunk)
                    pos += max_chunk
                    if pos < len(body):
                        time.sleep(0.5)
                tbody = "".join(chunks)
            else:
                tbody = translate_text(body, locale, session)
            if tbody:
                body = tbody

        result = f"---\n{fm_text}\n---\n{body}" if fm_text else body
        body_check = re.sub(r'---\s*\n.*?\n---\s*\n', '', result, flags=re.DOTALL) if fm_text else result
        if has_chinese(body_check):
            fail += 1
            print(f"  [{i+1}/{total}] FAIL {rel}", flush=True)
            # Still write (with whatever we have) rather than leave Chinese
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(result, encoding="utf-8")
        else:
            ok += 1
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(result, encoding="utf-8")

    print(f"[{locale}] Done: {ok} OK, {fail} FAIL, {skip} SKIP ({total} total)", flush=True)
    return ok, fail, skip


if __name__ == "__main__":
    total_ok = total_fail = 0
    for loc in LOCALES:
        ok, fail, _ = process_locale(loc)
        total_ok += ok
        total_fail += fail
        time.sleep(1)
    print(f"\nGRAND TOTAL: {total_ok} translated, {total_fail} failed")
