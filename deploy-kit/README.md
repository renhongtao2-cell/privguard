# PrivGuard — Privacy-First Local Watermark Remover

Remove image watermarks and backgrounds **100% in your browser**. No uploads, no server, no third-party GPU. Built for regulated teams that legally cannot send client files to a third party.

[🌐 Live web app](https://privguard.pages.dev) · [🟢 Edge Add-ons](https://microsoftedge.microsoft.com/addons) · [🦊 Firefox AMO](https://addons.mozilla.org)

## Why PrivGuard

- 🔒 **100% local** — files never leave the device; there is no upload endpoint
- 🧽 **Watermark remover** — brush over the mark, inpaint on-device (OpenCV.js)
- 🎯 **Background remover** — cut out people/products with an on-device AI model (@imgly)
- 🏢 **Compliance by architecture** — no Art. 28 sub-processor, no cross-border transfer
- 🆓 **Free, no account required**

## How it works

1. Pick a file (read locally, no network request)
2. The open-source engine loads once, then runs on-device
3. WASM/ONNX computes the result on your machine
4. You download the output — we keep nothing

## Tools

| Tool | Status | Engine |
|------|--------|--------|
| Watermark Remover | ✅ Live | OpenCV.js (inpaint) |
| Background Remover | ✅ Live | @imgly/background-removal |
| AI Upscaler | 🔜 Planned | UpscalerJS |
| Video Transcode | 🔜 Planned | ffmpeg.wasm |

## Self-host

The web app is a static build — drop it on any static host or your own intranet. Team & Enterprise plans include a self-host license.

## Privacy

No uploads, by design. See [privacy.html](privacy.html).

## License

MIT-licensed open-source engines (OpenCV.js, @imgly, ffmpeg.wasm), client-side only.
