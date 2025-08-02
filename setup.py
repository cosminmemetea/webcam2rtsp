from setuptools import setup, find_packages

setup(
    name="webcam2rtsp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pygobject"],
    entry_points={
        "console_scripts": [
            "webcam2rtsp=webcam2rtsp.__main__:main"
        ]
    },
    description="RTSP H.264 webcam streamer for macOS using GStreamer",
    author="Memetea Cosmin",
    python_requires=">=3.7",
)
