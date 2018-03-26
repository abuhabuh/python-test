import math
import threading
import time

"""
queue's list needs to trim itself
"""

LIMIT = 2
MATCHES = []


class QueueException(Exception):
  pass


class Node:
  def __init__(self, t):
    self.t = t
    self.next = None


class BlockingQueue:
  def __init__(self, name, offset_list):
    self.name = name
    self.offset_list = offset_list
    self.idx = 0
    self.base = 0

  def poll(self):
    if self.idx >= len(self.offset_list):
      return (None, None)

    return_time = self.base + self.offset_list[self.idx]
    self.idx += 1

    return (return_time, 'a')



def read_and_match(source_queue, my_queue, match_queue):

  all_matches = []

  while True:
    t, _ = source_queue.poll()
    if t is None:
      break
    get_matches(t, match_queue, source_queue.name)
    
    n = Node(t)
    my_queue.set_root(n)
    my_queue.drop_old(match_queue.top(), LIMIT)


def get_matches(t, match_seen, qname):
  trim = False
  node = match_seen.root
#  if node is not None:
#    print qname + ': starting at ' + str(node.t)

  count = 0
  while node is not None:
    count += 1
    if t > node.t and t - node.t > LIMIT:
      trim = True
      break
    if math.fabs(t - node.t) <= LIMIT:
      MATCHES.append((t, node.t))
    node = node.next

#  print qname + ' - count: ' + str(count)

  if trim:
    # print qname + ' - trim at ' + str(node.t)
    node.next = None

def is_match(t1, t2):
  # print 'try match: %s - %s' % (t1, t2)
  if math.fabs(t1 - t2) <= 1:
    return True
  return False


l = [3,4,5,5,5,5,5,4,3]
sum = 0
for i in l:
  sum += i
print 'sum: ' + str(sum)

q1 = BlockingQueue('q1', [1,2,3,4,5,6,7,8,9])
q2 = BlockingQueue('q2', [1,2,3,4,5,6,7,8,9])
# q1 = BlockingQueue('q1', [1,2,3,4])
# q2 = BlockingQueue('q2', [1,2,3,4])

class SeenLinkedList:
  def __init__(self):
    self.root = None
    self.lock = threading.Lock()

  def drop_old(self, ref_val, LIMIT):
    n = self.root
    while n is not None:
      if n.t < ref_val and ref_val - n.t > LIMIT:
        n.next = None
        return
      n = n.next

  def set_root(self, n):
    with self.lock:
      # TODO: here
      # - just implement this and run
      if self.root is None:
        self.root = n
      else:
        n.next = self.root
        self.root = n

  def top(self):
    if self.root is not None:
      return self.root.t
    return None
  
  def __str__(self):
    ptr = self.root
    out_str = ''
    while ptr is not None:
      out_str += str(ptr.t) + ' -> '
      ptr = ptr.next
    return out_str


seen_items_root1 = SeenLinkedList()
seen_items_root2 = SeenLinkedList()

t1 = threading.Thread(target=read_and_match, args=(q1, seen_items_root1, seen_items_root2))
t2 = threading.Thread(target=read_and_match, args=(q2, seen_items_root2, seen_items_root1))

t1.start()
t2.start()

t1.join()
t2.join()
print '1'
print str(seen_items_root1)
print '2'
print str(seen_items_root2)
print 'num matches: %d' % len(MATCHES)
print '== matches =='
print MATCHES
