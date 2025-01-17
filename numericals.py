# Description:
# You are given an input string.

# For each symbol in the string if it's the first character occurence, replace it with a '1', else replace it with the amount of times you've already seen it...

# But will your code be performant enough?

# Examples:
# input   =  "Hello, World!"
# result  =  "1112111121311"

# input   =  "aaaaaaaaaaaa"
# result  =  "123456789101112"
# There might be some non-ascii characters in the string.

def numericals(s):
    h = {}
    res = ''

    for ch in s:
      if ch in h:
        h[ch] += 1
      else:
        h[ch] = 1
      res += str(h[ch])

    return res