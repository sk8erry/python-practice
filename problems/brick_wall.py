#test_case = [[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]]
#test_case = [[10000],[10000],[10000]]
test_case = [[6], [6], [2, 4], [6], [1, 2, 2, 1], [6], [2, 1, 2, 1], [1, 5], [4, 1, 1], [1, 4, 1], [4, 2],
             [3, 3], [2, 2, 2], [5, 1], [5, 1], [6], [4, 2], [1, 5], [2, 3, 1], [4, 2], [1, 1, 4], [1, 3, 1, 1],
             [2, 3, 1], [3, 3], [3, 1, 1, 1], [3, 2, 1], [6], [3, 2, 1], [1, 5], [1, 4, 1]]
def brickwall(test_case):
    length = 0
    counter = 0
    lowest_count = 10000
    i = sum(test_case[0]) - 1

    for element in test_case:
        length += len(element)
    if length == len(test_case): return len(test_case)
    else: pass

    while counter < i:

        running_count = 0

        for brick in test_case:
            if brick[0] != 1:
                running_count += 1
            else: pass


        for element in test_case:
            if element[0] > 1:
                element[0] = element[0] - 1
            else: del element[0]
            print (test_case)

        if running_count < lowest_count:
            lowest_count = running_count
        print(running_count, lowest_count)
        counter += 1

    return lowest_count

print (brickwall(test_case))
