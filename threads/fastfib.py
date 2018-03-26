import threading


class Val:
  def __init__(self):
    self.n = None

def fib(n, val):
  if n == 1 or n == 2:
    return 1

  v1 = Val()
  v2 = Val()
  t1 = threading.Thread(target=fib, args=(n-1,v1))
  t2 = threading.Thread(target=fib, args=(n-2,v2))
  
  t1.start()
  t2.start()
  t1.join()
  t2.join()

  val.n = v1.n + v2.n


v = Val()
fib(34, v)

print 'Final: ' + str(v.n)
