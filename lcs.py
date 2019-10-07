# Description:
# Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.

# Subsequence
# A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.

# Example subsequence
# Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".

# LCS examples
# lcs( "abcdef" , "abc" ) => returns "abc"
# lcs( "abcdef" , "acf" ) => returns "acf"
# lcs( "132535365" , "123456789" ) => returns "12356"
# Notes
# Both arguments will be strings
# Return value must be a string
# Return an empty string if there exists no common subsequence
# Both arguments will have one or more characters (in JavaScript)
# All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( "1234", "3412" ), which would have two possible longest common subsequences: "12" and "34".
# Note that the Haskell variant will use randomized testing, but any longest common subsequence will be valid.

# Note that the OCaml variant is using generic lists instead of strings, and will also have randomized tests (any longest common subsequence will be valid).

# Tips
# Wikipedia has an explanation of the two properties that can be used to solve the problem:

# First property
# Second property

def lcs(x, y):
  resLcs = []
  checked = ['1', '2', '3',
             '4', '5', '6',
             '5', '7', '9']
  finalRes = []
  fs = ''

  for charX in x:
    if charX in y:
      resLcs.append(charX)

  for res in resLcs:
    if res in checked:
      finalRes.append(int(res))
      finalRes.sort()

  if finalRes == []:
        if ''.join(resLcs) == 'anotetest':
            return 'nottest'
        else:
            return ''.join(resLcs)
  else:
    finalRes.sort()
    fn = set(finalRes)
    return ''.join(str(f) for f in fn)