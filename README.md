# SBS Player

A lightweight VR video player for your phone's browser. It plays side-by-side (SBS) 180° and 360° VR videos as a normal "magic window" view: swipe with your finger to look around, no headset needed.

**▶ Open the player: <https://benegi-94.github.io/sbs-player/>**

**Your videos stay on your device.** Files are opened locally from your phone's storage and are never uploaded anywhere. There is no server, no account, no tracking.

## Features

- **Swipe to look around**: the image follows your finger; the view stops at the edge of a 180° image
- **Pinch to zoom**, double-tap to reset the view
- **Formats**: 180°, 360° or flat projection; side-by-side, top/bottom or mono layout
- **Playback controls**: play/pause, seek bar, skip ±15 seconds
- **Resume**: remembers where you stopped in each video
- **Fullscreen** with automatic landscape rotation (Android)
- **Installable app (PWA)**: add it to your home screen; it works offline after the first visit
- Single HTML file, no frameworks, no build step, rendered with plain WebGL

## Usage

The interface is currently in German.

1. Open the player in your phone's browser.
2. Optional: tap **App installieren** (*Install app*, Android Chrome) or *Share → Add to Home Screen* (iPhone Safari).
3. Tap **Video öffnen** (*Open video*) and pick a video file from your device.
4. Swipe to look around, pinch to zoom, double-tap to reset.

Tap the video to show or hide the controls. The menus at the top switch the projection and layout if a video isn't 180° side-by-side.

## Compatibility

- Works in current Chrome (Android) and Safari (iOS), as well as desktop browsers (mouse drag and wheel zoom).
- Playback depends on what your device can decode: H.264 runs almost everywhere, H.265/HEVC only on devices with hardware support. 4K at 60 fps needs a fairly recent phone.
- Fullscreen and orientation lock are not available on iPhone; use *Add to Home Screen* instead.

## Repository layout

| Path | Purpose |
|---|---|
| `web/index.html` | The player |
| `web/manifest.webmanifest` | App name, icons, display mode |
| `web/sw.js` | Offline cache for the app files (videos are never cached) |
| `web/icons/` | App icons |
| `index.html` | Redirects the site root to `web/` |
| `tools/make_icons.py` | Regenerates the icons (plain Python, no packages needed) |

## Hosting your own copy

Everything is static. Fork the repository and enable GitHub Pages (*Settings → Pages → Deploy from a branch → main / root*), or serve the files from any HTTPS host.

When you change a file in `web/`, bump `VERSION` in `web/sw.js` so installed copies pick up the update.
