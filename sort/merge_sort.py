array = [4,2,6,8,10,3,12,12,4,6]

def sort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j
        while array[i-1] > key and i > 0:
            array[i] = array[i-1]
            i = i - 1
        array[i] = key
        print (j)
    return array

print (sort(array))
