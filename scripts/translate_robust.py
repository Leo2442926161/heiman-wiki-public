#!/usr/bin/env python3
"""Robust translation with checkpoint/resume, retry, and error handling."""

import json, os, re, sys, time, urllib.parse, urllib.request, ssl
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
I18N_DIR = BASE_DIR / "i18n"
LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]
PROXY = "http://127.0.0.1:11000"
STATE_FILE = BASE_DIR / ".translate_state.json"

CN_PATTERN = re.compile(r'[\u4e00-\u9fff]')
PRESERVE = {"海曼": "Heiman", "海曼科技": "Heiman Technology"}

def has_chinese(text):
    return bool(CN_PATTERN.search(text))

def translate_text(text, target):
    if not text.strip():
        return text
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": "zh-CN", "tl": target, "dt": "t", "q": text}
    full_url = url + "?" + urllib.parse.urlencode(params)
    for attempt in range(8):
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(full_url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            })
            ph = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
            opener = urllib.request.build_opener(ph)
            with opener.open(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                result = "".join(p[0] for p in data[0])
            for ch, en in PRESERVE.items():
                result = result.replace(ch, en)
            if has_chinese(result):
                time.sleep(3 * (attempt + 1))
                continue
            return result
        except Exception as e:
            if attempt < 7:
                delay = 2 * (attempt + 1)
                time.sleep(delay)
                continue
            return None
    return None

def process_file(src_path, target_dir, locale, max_retries=3):
    rel = src_path.relative_to(DOCS_DIR)
    target_path = target_dir / rel

    if target_path.exists():
        try:
            content = target_path.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n.*?\n---\s*\n", content, re.DOTALL)
            body = content[m.end():] if m else content
            if not has_chinese(body):
                return "skip"
        except Exception:
            pass

    content = src_path.read_text(encoding="utf-8")
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
            if "title" in fm and fm["title"] and has_chinese(fm["title"]):
                for r in range(max_retries):
                    t = translate_text(fm["title"], locale)
                    if t:
                        fm["title"] = t
                        break
                    time.sleep(3)
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
        except Exception:
            pass

    # Translate body
    if body.strip() and has_chinese(body):
        chunk_size = 2500
        if len(body) > chunk_size:
            chunks = []
            for pos in range(0, len(body), chunk_size):
                chunk = body[pos:pos + chunk_size]
                for r in range(max_retries):
                    tr = translate_text(chunk, locale)
                    if tr:
                        chunks.append(tr)
                        break
                    time.sleep(3)
                else:
                    chunks.append(chunk)
                time.sleep(0.3)
            tbody = "".join(chunks)
        else:
            tbody = None
            for r in range(max_retries):
                tbody = translate_text(body, locale)
                if tbody:
                    break
                time.sleep(3)
            if tbody:
                body = tbody

    result = f"---\n{fm_text}\n---\n{body}" if fm_text else body
    body_check = re.sub(r'---\s*\n.*?\n---\s*\n', '', result, flags=re.DOTALL) if fm_text else result
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(result, encoding="utf-8")
    if has_chinese(body_check):
        return "fail"
    return "ok"

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}

def main():
    state = load_state()
    src_files = sorted(DOCS_DIR.rglob("*.md"))

    for locale in LOCALES:
        if locale in state and state[locale].get("done"):
            print(f"[{locale}] Already completed, skip", flush=True)
            continue

        target_dir = I18N_DIR / locale / "docusaurus-plugin-content-docs" / "current" / "docs"
        last_idx = state.get(locale, {}).get("last_idx", -1)
        stats = {"ok": 0, "fail": 0, "skip": 0}

        print(f"\n[{locale}] Starting from index {last_idx+1}...", flush=True)

        for i, src_path in enumerate(src_files):
            if i <= last_idx:
                # Re-count from existing files
                rel = src_path.relative_to(DOCS_DIR)
                tgt = target_dir / rel
                if tgt.exists():
                    try:
                        c = tgt.read_text(encoding="utf-8")
                        m = re.match(r"^---\s*\n.*?\n---\s*\n", c, re.DOTALL)
                        b = c[m.end():] if m else c
                        if has_chinese(b):
                            stats["fail"] += 1
                        else:
                            stats["skip"] += 1
                    except:
                        pass
                continue

            try:
                result = process_file(src_path, target_dir, locale)
                if result == "ok":
                    stats["ok"] += 1
                elif result == "fail":
                    stats["fail"] += 1
                else:
                    stats["skip"] += 1
            except Exception as e:
                stats["fail"] += 1
                print(f"  ERROR processing {src_path.relative_to(DOCS_DIR)}: {e}", flush=True)

            if (i + 1) % 10 == 0:
                total = stats["ok"] + stats["fail"] + stats["skip"]
                print(f"  [{locale}] [{i+1}/{len(src_files)}] ok={stats['ok']} fail={stats['fail']} skip={stats['skip']}", flush=True)
                state[locale] = {"last_idx": i, "done": False}
                save_state(state)

        print(f"[{locale}] Done: {stats['ok']} OK, {stats['fail']} FAIL, {stats['skip']} SKIP", flush=True)
        state[locale] = {"last_idx": len(src_files) - 1, "done": True}
        save_state(state)
        time.sleep(2)

    print("\nALL DONE!", flush=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"FATAL ERROR: {e}", flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)
