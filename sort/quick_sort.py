#QuickSort

import random
import copy

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array

test_array = [2,4,3,7657,23,67,34,8,322,6,3,6546]
print(sort(test_array))
