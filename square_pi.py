# Description:
# Everybody loves pi, but what if pi were a square? Given a number of digits digits, find the smallest integer whose square is greater or equal to the sum of the squares of the first digits digits of pi, including the 3 before the decimal point.

# Note: Test cases will not extend beyond 100 digits; the first 100 digits of pi are pasted here for your convenience:

import math
from functools import reduce

def square_pi(digits):
  d='31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'    
  return math.floor(math.ceil(reduce(lambda s,i: s+int(i)**2,[r for r in ''.join(r for r in d[0:digits].split())],0) **0.5))

square_pi(3)