from picamera import PiCamera
from UartSubscriber import UartSubscriber
from DebugSubscriber import DebugSubscriber
from ByteOutstream_Thread import ByteOutstream
from StreamObject import StreamObject
from threading import Timer
from SocketSubscriber import SocketSubscriber

def main():
    
    # Instantiate subscribers
    uart = UartSubscriber()
    debug = DebugSubscriber()
    with SocketSubscriber('104.199.128.49', 1337) as socket:
        '''Test code to close socket after sending for 15s'''
        socketTimeoutTimer = Timer(15.0, socket.disableOutput())
        socketTimeoutTimer.start()
        # Instantiate streams and streaminer thread 
    #     stream = BytesIO()
        stream = StreamObject()
        streamerThread = ByteOutstream(stream)
        streamerThread.subscribe(uart)
        streamerThread.subscribe(debug)
        streamerThread.subscribe(socket)
    
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording(stream, format='h264', quality=23)
    #     camera.start_recording('video.h264')
        streamerThread.start()
        camera.wait_recording(15)
#     
#     camera.stop_recording()


if __name__ == "__main__":
    main()