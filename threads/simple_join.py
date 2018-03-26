"""Simple threading / join illustration
"""
import threading
import time

def wait(name, n_sec):
    print '%s begin wait %d' % (name, n_sec)
    for x in range(0, n_sec):
      print '%s sleep 1' % (name,)
      time.sleep(1)
    print '%s done waiting' % (name,)


t1 = threading.Thread(name='t1', target=wait, args=('t1', 10))
t2 = threading.Thread(name='t2', target=wait, args=('t2', 10))

t1.start()
t2.start()

print 'join t1'
t1.join()
print 't1 join done'

print 'join t2'
t2.join()
print 't2 join done'


