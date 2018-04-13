import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 8888))


n = 0


def monitor():
    global n
    while 1:
        time.sleep(1)
        print '%s req/s' % n
        n = 0


threading.Thread(target=monitor).start()


while 1:
    s.sendall("1")
    data = s.recv(100)
    n += 1
