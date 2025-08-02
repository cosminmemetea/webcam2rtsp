# 📡 webcam2rtsp

**webcam2rtsp** is a Python package for macOS that streams your webcam over RTSP using H.264 encoding and GStreamer.

🖥️ URL: `rtsp://localhost:8851/webcam1`

---

## ✅ Features

- RTSP server accessible on `localhost:8851`
- Streams using system webcam with H.264 encoding
- Easy to install and run in a virtual environment
- Compatible with GStreamer-enabled players (VLC, FFplay, etc.)

---

## 🚀 Getting Started (macOS only)

### 1. Install GStreamer (macOS)

```bash
brew install gstreamer gst-plugins-base gst-plugins-good gst-libav gst-plugins-bad gst-plugins-ugly pygobject3
```

### 2. Add Environment Variables Temporarily
In your terminal (in the project folder):

```bash
export DYLD_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_LIBRARY_PATH
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
export GI_TYPELIB_PATH=/opt/homebrew/lib/girepository-1.0
```



### 3. (Optional) Add Environment Variables Permanently
Edit your ~/.zshrc (or ~/.bash_profile):

```bash
nano ~/.zshrc
```
And copy in the end of the .zshrc and .bash_profile at the end.
```bash
export DYLD_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_LIBRARY_PATH
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
export GI_TYPELIB_PATH=/opt/homebrew/lib/girepository-1.0
```

Good luck saving the file using using nano editor!


### 4. Clone and run

```bash
git clone https://github.com/cosminmemetea/webcam2rtsp.git
cd webcam2rtsp
python3 -m venv venv
source venv/bin/activate
pip install -upgrade pip
pip install -r requirements.txt
pip install -e .
python -m webcam2rtsp
```

You can now open the stream at:

```bash
rtsp://localhost:8851/webcam1
```

With:

VLC → Open Network Stream

FFplay → ffplay rtsp://localhost:8851/webcam1

### 5. (Optional) Create a macOS .command launcher

Let’s automate this. Create a file named run_webcam2rtsp.command in your project folder:


```bash
touch run_webcam2rtsp.command
chmod +x run_webcam2rtsp.command
```


