"""Read from and write to file
Use a mutex lock
"""
import threading
import time

NUM_THREADS = 2
LOOP = 4000

fname = 'out.txt'
lock = threading.Lock()

f = open(fname, 'w+')
f.close()

def inc(name, fname):
  with lock:
    f = open(fname, 'r+')
    val = f.read()
    if not val:
      val = 0
    else:
      val = int(val)
    val += 1
    f.seek(0)
    f.truncate()
    f.write(str(val))
    f.close()

def increment(name, loop_num):
  for i in range(0, loop_num):
    inc(name, fname)

threads = []
for i in range(0, NUM_THREADS):
  t = threading.Thread(target=increment, args=(i, LOOP,))
  t.start()
  threads.append(t)
for t in threads:
  t.join()

print 'EXP: %d' % (NUM_THREADS * LOOP)
f = open(fname, 'r')
print 'NUM: %s' % f.read()
f.close()

