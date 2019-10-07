# Given an array, find the int that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
  count = 0
  for i in range(len(seq)):
    for x in range(len(seq)):
      # print(seq[i])
      if(seq[i] == seq[x]):
        count = count + 1
    if(count %2 != 0):
        print(seq[i])
        return seq[i]
  
  count = 0