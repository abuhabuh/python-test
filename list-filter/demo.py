"""
Demos method of list filtering using yields so that complex loops
can be boiled down to smaller, functional components
"""
master_list = list(range(1, 100))


def evens_only(input_list):
  for x in input_list:
    if x % 2 == 0:
      yield x

def eights_only(input_list):
  for x in input_list:
    if x % 8 == 0:
      yield x


for x in eights_only(evens_only(master_list)):
  print(x)

