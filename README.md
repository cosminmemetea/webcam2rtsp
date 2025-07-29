# 📡 webcam2rstp

**webcam2rstp** is a cross-platform Python package that streams your laptop's webcam as an **RTSP (H.264)** video feed using **GStreamer**.

📺 Stream your webcam via:

bash```
rtsp://localhost:8854/test
```


---

## ✅ Features

- RTSP server accessible on `localhost:8854`
- Auto-detects operating system (Linux, macOS, Windows)
- Streams using system webcam with H.264 encoding
- Easy to install and run in a virtual environment
- Compatible with GStreamer-enabled players (VLC, FFplay, etc.)

---

## 🚀 Quick Start

### 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate         # On macOS/Linux
venv\Scripts\activate            # On Windows
```

### 2. Install Python dependencies
pip install -r requirements.txt
pip install -e .


🪟 Windows Setup
1. Install GStreamer (Full MSVC x64)
Download from:
👉 https://gstreamer.freedesktop.org/download/

Install both:

Runtime Installer

Development Installer

Typical path: C:\gstreamer\1.0\x86_64\

2. Set environment variables (PowerShell)

bash```
$env:PATH += ";C:\gstreamer\1.0\x86_64\bin"
$env:GI_TYPELIB_PATH = "C:\gstreamer\1.0\x86_64\lib\girepository-1.0"
(You can add these to system environment variables permanently.)
```

3. Test GStreamer
bash```
gst-launch-1.0 ksvideosrc ! videoconvert ! autovideosink
If webcam window appears, you're good to go!
```



python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .
