"""Threaded server example.

Server that demonstrates threads vs processes
"""
import datetime
import socket
import threading
import multiprocessing

print '# CPUs %d' % multiprocessing.cpu_count()

NUM_CLIENTS = 50
NUM_REQ = 10
HOST = '127.0.0.1'
PORT = 8888


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def run_worker(conn, client_addr):
    """Receive connection and send a ping back
    """
    # print 'worker started'
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(str(fib(int(data))))
    # print 'worker finished'


def run_server():
    print 'Server started\n'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    # Argument to listen() means max number of queued connections to queue
    # up before refusing more conns
    s.listen(1)

    workers = []
    num_c = 0

    while num_c < NUM_CLIENTS:
        # Wait for and accept a connection with accept()
        conn, addr = s.accept()
        num_c += 1
        worker = threading.Thread(target=run_worker, args=(conn, addr))
        # worker = multiprocessing.Process(target=run_worker, args=(conn, addr))
        worker.start()
        workers.append((worker, conn))

    print 'joining workers'
    for t, _ in workers:
        t.join()
    print 'workers joined'
    for _, conn in workers:
        conn.close()
    print 'Server exit\n'


def run_client(name):
    # print 'Client %s started' % name

    def connect_socket():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connected = False
        while not connected:
            try:
                s.connect((HOST, PORT))
                connected = True
            except Exception:
                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s

    s = connect_socket()

    ts = datetime.datetime.now()
    for x in range(0, NUM_REQ):
        sent = False
        while not sent:
            try:
                s.sendall("20")
                s.recv(1024)
                sent = True
            except Exception as e:
                print '%s failed sendall -- reconnecting...  exception %s' % (name, e)
                s = connect_socket()
    te = datetime.datetime.now()

    s.close()
    print '%s: %d req processed in %s' % (name, NUM_REQ, te - ts)


if __name__ == '__main__':
    threads = []

    server_t = threading.Thread(target=run_server)
    # server_t = multiprocessing.Process(target=run_server)
    server_t.start()
    threads.append(server_t)

    for x in range(0, NUM_CLIENTS):
        cname = 'c%d' % x
        c = threading.Thread(target=run_client, args=(cname,), name=cname)
        # c = multiprocessing.Process(target=run_client, args=(cname,), name=cname)
        c.start()
        threads.append(c)

    for t in threads:
        t.join()
