'''
Created on Jan 27, 2018

@author: root
'''
import socket
import subprocess
from threading import Thread
from threading import Timer
from display_thread import DisplayThread
from queue import Queue

def main():

    # Start a client socket and pull data from server
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('104.199.128.49', 8082)
    
    # Accept a single connection and make a file-like object out of it
    connection = client_socket.connect(server_address)
    try:
        # Run a viewer with an appropriate command line. Uncomment the mplayer
        # version if you would prefer to use mplayer instead of VLC
        cmdline = ['vlc', '--demux', 'h264', '-']
        #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
        player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
        
        videoBuffer = Queue(20000)
        displayThread = DisplayThread(player, videoBuffer, 20000, client_socket)
        
        displayThread.start()
        while True:
            # Repeatedly read 1k of data from the connection and write it to
            # the media player's stdin
            data = client_socket.recv(1024)
#             print("Data read")
            if not data:
                break
            player.stdin.write(data)
#             print(data)

    finally:
        client_socket.close()
        player.terminate()
    
if __name__ == '__main__':
    main()