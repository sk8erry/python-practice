from random import *

test_case = []
for k in range(0,9):
    test_case.append(randint(0,99))

def sort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j
        while array[i-1] > key and i > 0:
            array[i] = array[i-1]
            i = i - 1
        array[i] = key
    return array

print (sort(test_case))
