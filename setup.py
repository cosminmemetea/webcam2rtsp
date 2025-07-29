from setuptools import setup, find_packages

setup(
    name="webcam2rtsp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pygobject"],
    entry_points={
        "console_scripts": [
            "webcam-rtsp=webcam2rtsp.streamer:main"
        ]
    },
    description="Cross-platform RTSP H.264 webcam streamer using GStreamer",
    author="Your Name",
    python_requires=">=3.7",
)
