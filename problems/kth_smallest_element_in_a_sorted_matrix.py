'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
'''

def solution(matrix, k):
    if len(matrix) == 1: return matrix[0][0]
    counter = 0
    sortedList = []
    firstCol = []
    while counter < k:
        firstCol = [row[0] for row in matrix]
        print(firstCol)
        min1stCol = min(firstCol)
        if len(matrix[firstCol.index(min1stCol)]) > 1:
            matrix[firstCol.index(min1stCol)].pop(0)
        else:
            matrix.pop(firstCol.index(min1stCol))
        counter += 1
        sortedList.append(min1stCol)
        print(sortedList)
    return sortedList[k-1]

matrix = [[1,2],[1,3]]
k = 1
print(solution(matrix, k))