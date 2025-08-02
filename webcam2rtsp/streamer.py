import platform
import sys
import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject

class WebcamRTSPServer:
    def __init__(self, port=8854, mount_point="/webcam1"):
        Gst.init(None)

        self.port = str(port)
        self.mount_point = mount_point
        self.server = GstRtspServer.RTSPServer()
        self.server.set_service(self.port)

        factory = GstRtspServer.RTSPMediaFactory()
        factory.set_launch(self._get_pipeline())
        factory.set_shared(True)

        self.server.get_mount_points().add_factory(self.mount_point, factory)
        self.server.attach(None)

        print(f"[✓] RTSP stream at rtsp://localhost:{self.port}{self.mount_point}")

    def _get_pipeline(self):
        os_name = platform.system().lower()
        
        if os_name == "darwin":
            source = "avfvideosrc device-index=0"
        else:
            raise Exception(f"Unsupported OS: {os_name}")

        pipeline = (
            f"{source} ! "
            "video/x-raw,width=640,height=480,framerate=30/1 ! "
            "videoconvert ! "
            "x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! "
            "rtph264pay config-interval=1 name=pay0 pt=96"
        )
        print(f"[i] GStreamer pipeline:\n    {pipeline}")
        return pipeline

    def run(self):
        loop = GObject.MainLoop()
        try:
            loop.run()
        except KeyboardInterrupt:
            print("[✗] Stopped.")