# Description:
# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(source_array):

    for i in range(0, len(source_array)):
        for j in range(i, len(source_array)):
            if(source_array[i] % 2 == 1 and source_array[j] % 2 == 1):
                if(source_array[j] < source_array[i]):
                    aux = source_array[i]
                    source_array[i] = source_array[j]
                    source_array[j] = aux
    return source_array