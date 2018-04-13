import socket
import threading


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def worker(conn, addr):
    print 'started worker'
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall('%s\n' % str(fib(int(data))))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8888))

s.listen(0)

while 1:
    print 'listening for conn'
    conn, addr = s.accept()
    print 'launching worker...'
    threading.Thread(target=worker, args=(conn, addr)).start()
    print 'finished launching worker'


s.close()
