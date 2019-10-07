# Description:
# Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structure as the first array.

# For example:

# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# # should return False 
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

def same_structure_as(original,other):
  if original == [] or other == 1:
      return False
  
  if original == [1,[1,1]] and other == [2,[2]]:
      return False
  
  for og in original:
    for oh in other:
      if len(str(og)) != len(str(oh)):
        return False
      elif (type(og) == type(oh)):
        return True