# PrivGuard 部署与上线指南

> 目标：把免费层（网页版 + 浏览器插件）真正上线，进入平台搜索流量池。
> 全部免费平台，零推广成本。

## 0. 前置账号（全部免费）

| 平台 | 用途 | 注册地址 |
|------|------|----------|
| Cloudflare | 网页版托管（自带索引/搜索流量） | https://dash.cloudflare.com/sign-up |
| Microsoft | Edge Add-ons 开发者（Windows 默认浏览器搜索流量） | https://partner.microsoft.com/dashboard/microsoftedge/ |
| Firefox | AMO 开发者 | https://addons.mozilla.org/developers/ |
| GitHub | 开源发布（开发者自然搜索 + 信任背书） | https://github.com |

## 1. Cloudflare Pages — 网页版上线（流量主入口）

```bash
cd E:/xiangmu/tuiguang/privguard
npm i -g wrangler
wrangler login            # 浏览器授权
wrangler pages deploy . --project-name=privguard
```

- 部署后获 `*.pages.dev` 域名，自动进入 Cloudflare 索引
- 可在 Cloudflare 后台绑自定义域名（如 `privguard.app`，需自有域名）
- 网页版含去水印 + 背景移除，是免费流量主入口

## 2. Edge Add-ons — 插件提交（Windows 自带搜索流量）

```bash
cd E:/xiangmu/tuiguang/privguard/edge
zip -r ../privguard-edge.zip . -x "*.DS_Store"
```

1. 打开 https://partner.microsoft.com/dashboard/microsoftedge/
2. 新建 Extension → 上传 `privguard-edge.zip`
3. 填名称/描述/关键词/分类（见 `STORE-LISTING.md`）
4. 传截图（见 `STORE-LISTING.md` 第四节）
5. 提交审核（通常 1–7 天，免费，无开发者费）

## 3. Firefox AMO — 插件提交

Firefox 用同一 MV3 manifest，但需在 `manifest.json` 加 gecko id：

```json
"browser_specific_settings": {
  "gecko": { "id": "privguard@yourapp.com" }
}
```

```bash
cd E:/xiangmu/tuiguang/privguard/edge
zip -r ../privguard-firefox.xpi .
```

1. 打开 https://addons.mozilla.org/developers/
2. Submit a New Add-on → 上传 `privguard-firefox.xpi`
3. 同 Edge 文案（见 `STORE-LISTING.md`）
4. 审核（自动 + 人工，约数天，免费）

## 4. GitHub 开源 — 开发者信任 + 搜索

```bash
cd E:/xiangmu/tuiguang/privguard
git init
git add .
git commit -m "PrivGuard: privacy-first local watermark remover"
gh repo create privguard --public --source=. --push
```

- README 见 `README.md`
- 开源本身带来开发者自然搜索与信任背书

## 附录：本地截图方法（商店必填）

1. 启动本地预览：`cd E:/xiangmu/tuiguang/privguard && python -m http.server 8766 --bind 127.0.0.1`
2. 浏览器打开 http://127.0.0.1:8766
3. 按 F12 → 设备工具栏（Ctrl+Shift+M）→ 设 1280×800
4. 对每屏截图另存 PNG（按 `STORE-LISTING.md` 第四节清单）
5. 插件 popup 截图：点工具栏 PrivGuard 图标，对弹窗截图
