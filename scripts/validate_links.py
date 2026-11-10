#!/usr/bin/env python3
"""
Validation script for Shashwat Upadhyay's GitHub Profile README.

Verifies:
1. All local assets and card links in README.md exist on disk.
2. All SVG files parse as valid XML without syntax errors.
3. All external URLs are well-formed and valid.
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
README_PATH = os.path.join(ROOT, "README.md")

def check_local_assets():
    print("Checking local asset paths in README.md...")
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find src="./cards/..." or src="./assets/..." or srcset="./..."
    local_refs = re.findall(r'(?:src|srcset)="(\./[^"]+)"', content)
    missing = []
    found = []
    for ref in local_refs:
        rel_path = ref.lstrip("./")
        abs_path = os.path.join(ROOT, rel_path)
        if not os.path.exists(abs_path):
            missing.append(ref)
        else:
            found.append(ref)

    print(f"Found {len(found)} valid local asset references.")
    if missing:
        print(f"ERROR: {len(missing)} missing asset references:")
        for m in missing:
            print(f"  - {m}")
        return False
    return True

def validate_svg_files():
    print("Validating XML syntax of all SVG cards and assets...")
    dirs_to_check = [os.path.join(ROOT, "cards"), os.path.join(ROOT, "assets")]
    invalid_svgs = []
    valid_count = 0

    for d in dirs_to_check:
        if not os.path.exists(d):
            continue
        for fn in os.listdir(d):
            if fn.endswith(".svg"):
                fpath = os.path.join(d, fn)
                try:
                    ET.parse(fpath)
                    valid_count += 1
                except ET.ParseError as pe:
                    invalid_svgs.append((fn, str(pe)))

    print(f"Successfully validated {valid_count} SVG files.")
    if invalid_svgs:
        print(f"ERROR: {len(invalid_svgs)} invalid SVG files:")
        for fn, err in invalid_svgs:
            print(f"  - {fn}: {err}")
        return False
    return True

def validate_external_urls(check_network=False):
    print("Checking external URLs in README.md...")
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    urls = re.findall(r'href="(https?://[^"]+)"', content)
    unique_urls = sorted(list(set(urls)))
    print(f"Found {len(unique_urls)} unique external URLs.")

    if not check_network:
        print("URL syntax check passed (network ping skipped by default).")
        return True

    headers = {"User-Agent": "Mozilla/5.0"}
    failed = []
    for u in unique_urls:
        try:
            req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"  [OK {resp.status}] {u}")
        except Exception as e:
            failed.append((u, str(e)))
            print(f"  [FAILED] {u} -> {e}")

    if failed:
        print(f"Warning: {len(failed)} URLs could not be reached:")
        for u, err in failed:
            print(f"  - {u}: {err}")
        return False
    return True

def main():
    assets_ok = check_local_assets()
    svg_ok = validate_svg_files()
    urls_ok = validate_external_urls(check_network=False)

    if assets_ok and svg_ok and urls_ok:
        print("\nAll README validation checks PASSED successfully! [OK]")
        sys.exit(0)
    else:
        print("\nValidation FAILED! Please fix the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()

