#!/usr/bin/env python3
"""Translate JSON i18n files (sidebar, navbar, footer, UI strings)."""

import json, os, re, sys, time, urllib.request, urllib.parse, ssl
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
I18N_DIR = BASE_DIR / "i18n"
PROXY = "http://127.0.0.1:11000"
LOCALES = ["de", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr"]

# Hard-coded translations for fixed terms (brand names, product names)
TERMS = {
    "海曼科技": "Heiman Technology",
    "海曼科技 Logo": "Heiman Technology Logo",
    "文档中心": None,  # translate per locale
    "博客": None,
    "官网": None,
    "文档": None,
    "产品与方案": None,
    "更多": None,
    "海曼简介": None,
    "产品类型": None,
    "智慧消防": None,
    "智慧燃气": None,
    "智慧养老": None,
    "联系我们": None,
}

CN_PATTERN = re.compile(r'[\u4e00-\u9fff]')

def has_any_chinese(text):
    return bool(CN_PATTERN.search(text))

def translate_text(text, target):
    if not text.strip() or not has_any_chinese(text):
        return text
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": "zh-CN", "tl": target, "dt": "t", "q": text}
    full_url = url + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(full_url, headers={"User-Agent": "Mozilla/5.0"})
            ph = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
            opener = urllib.request.build_opener(ph)
            with opener.open(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                result = "".join(p[0] for p in data[0])
            if has_any_chinese(result):
                time.sleep(1)
                continue
            return result
        except Exception:
            if attempt < 4:
                time.sleep(1)
                continue
    return text  # fallback to original

def process_json(locale):
    files_to_process = [
        "docusaurus-plugin-content-docs/current.json",
        "docusaurus-theme-classic/navbar.json",
        "docusaurus-theme-classic/footer.json",
        "code.json",
    ]

    for fname in files_to_process:
        path = I18N_DIR / locale / fname
        if not path.exists():
            continue

        data = json.loads(path.read_text(encoding="utf-8"))
        modified = False

        for key in data:
            val = data[key]
            if isinstance(val, dict) and "message" in val:
                msg = val["message"]
                if has_any_chinese(msg):
                    translated = translate_text(msg, locale)
                    if translated != msg and not has_any_chinese(translated):
                        val["message"] = translated
                        modified = True
                        print(f"  [{locale}] {key}: {msg[:30]}... -> {translated[:30]}...", flush=True)

        if modified:
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"[{locale}] JSON files done", flush=True)


if __name__ == "__main__":
    for loc in LOCALES:
        print(f"\n[{loc}] Processing JSON files...", flush=True)
        process_json(loc)
        time.sleep(1)
    print("\nAll JSON files done!", flush=True)
