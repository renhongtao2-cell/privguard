#!/usr/bin/env python3
"""构建 PrivGuard 各平台上架包：Edge zip / Firefox xpi。"""
import json, os, zipfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # privguard/
EDGE = os.path.join(ROOT, "edge")
OUT = os.path.join(ROOT, "deploy-kit")
os.makedirs(OUT, exist_ok=True)

def zip_dir(src, dest, extra_manifest=None):
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(src):
            for f in files:
                if f == ".DS_Store":
                    continue
                full = os.path.join(root, f)
                rel = os.path.relpath(full, src)
                if extra_manifest and rel == "manifest.json":
                    data = json.load(open(full, encoding="utf-8"))
                    data.update(extra_manifest)
                    z.writestr(rel, json.dumps(data, indent=2, ensure_ascii=False))
                else:
                    z.write(full, rel)
    print(f"built {dest} ({os.path.getsize(dest)} bytes)")

# 1) Edge: 直接用 edge/ 原样打包
zip_dir(EDGE, os.path.join(OUT, "privguard-edge.zip"))

# 2) Firefox: 加 gecko id 后打包为 .xpi
ff_manifest = {"browser_specific_settings": {"gecko": {"id": "privguard@renhongtao2-cell.com"}}}
zip_dir(EDGE, os.path.join(OUT, "privguard-firefox.xpi"), extra_manifest=ff_manifest)

print("done")
