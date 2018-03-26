import logging
import os


LOG_FILE = 'logging-test.log'


logging.basicConfig(filename=LOG_FILE, level=logging.INFO, filemode='w')

for x in range(1, 10):
  logging.info('asdf: %d' % x)
  
  with open(LOG_FILE, 'r') as rf:
    print '>>>>  ' + rf.read()

  os.remove(LOG_FILE)

#  with open(LOG_FILE, 'w') as wf:
#    pass
