"""Simplest server example - excepts one client connection and then exit
Uses INET sockets
"""
import socket
import threading
import time


def run_server():
    # HOST: listen to connections on any INET addr
    HOST = ''
    PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    # Argument to listen() means max number of queued connections to queue
    # up before refusing more conns
    s.listen(1)

    # Wait for and accept a connection with accept()
    conn, addr = s.accept()
    print 'Client connected at addr %s' % str(addr)
    while 1:
        data = conn.recv(1024)
        if not data:
            print 'Client disconnected'
            break
        print '> echo to client: %s' % data
        conn.sendall(data)

    conn.close()


def run_client():
    HOST = '127.0.0.1'
    PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.sendall("hello, world")

    data = s.recv(1024)
    s.close()
    print 'received %s' % data


if __name__ == '__main__':
    server_t = threading.Thread(target=run_server)
    client_t = threading.Thread(target=run_client)

    server_t.start()
    # hack to let server start
    time.sleep(2)
    client_t.start()

    server_t.join()
    client_t.join()
