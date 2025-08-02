from .streamer import WebcamRTSPServer

def main():
    server = WebcamRTSPServer()
    server.run()

if __name__ == "__main__":
    main()
