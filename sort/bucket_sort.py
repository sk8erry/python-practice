#Bucket Sort
import copy
import random

def bucketSort(array):
    bucket = [None] * (max(array) + 1)
    #Create a list with max(array) + 1 elements to store sorted numbers

    for x in array:
        bucket[x] = x

    bucket = [x for x in bucket if x != None]
    #Remove 'None in list'
    return bucket

def createRandomList(size):
    randomList = []
    for i in range(size):
        randomList.append(random.randint(1,1000))
    return randomList

testList = createRandomList(1000)
print(bucketSort(testList))
