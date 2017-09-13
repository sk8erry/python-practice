import random
import copy
def bubbleSort(a):
    indexCounter = 0
    innerLoopCounter = 1
    for innerloopCounter in range(len(a)-1):
        for indexCounter in range(len(a)-innerLoopCounter):
            if a[indexCounter] < a[indexCounter + 1]:
                a[indexCounter], a[indexCounter + 1] = a[indexCounter + 1], a[indexCounter]        
            else:
                pass
        indexCounter = 0
    return a

list = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
copyList = copy.copy(list)
print(copyList,bubbleSort(list))



