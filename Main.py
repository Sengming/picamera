from picamera import PiCamera
from UartSubscriber import UartSubscriber
from DebugSubscriber import DebugSubscriber
from ByteOutstream_Thread import ByteOutstream
from StreamObject import StreamObject
from threading import Timer
from SocketSubscriber import SocketSubscriber
import serial
from GpsSender import GpsReader
from queue import Queue

def main():
    # Start serial port and pass to gps sender:
    serialOutQueue = Queue(1000)
    serialPort = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
    gpsReader = GpsReader(serialPort, serialOutQueue)
    gpsReader.start()
    # Instantiate subscribers
    uart = UartSubscriber()
    debug = DebugSubscriber()
    with SocketSubscriber('104.199.128.49', 8081) as socket:
#     with SocketSubscriber('192.168.0.24', 8507) as socket:
        '''Test code to close socket after sending for 15s'''
        # Instantiate streams and streaminer thread 
    #     stream = BytesIO()
        stream = StreamObject()
        streamerThread = ByteOutstream(stream)
#         streamerThread.subscribe(uart)
#         streamerThread.subscribe(debug)
        streamerThread.subscribe(socket)
     
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording(stream, format='h264', quality=23)
#         socketTimeoutTimer = Timer(10, stream.printBytes)
#         socketTimeoutTimer.start()
#     camera.start_recording('video.h264')
        streamerThread.start()
        camera.wait_recording(96000)
#         print("Bytes written:"+stream.numberOfBytesWritten)
#                 camera.wait_recording(86400)
    camera.stop_recording()
#     print("Exited with")

if __name__ == "__main__":
    main()