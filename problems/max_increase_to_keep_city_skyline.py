'''
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
'''

def solution(grid):
    if len(grid) == 1: return grid[0][0]
    maxIncrease = 0
    maxX = []
    maxY = []
    indexX = 0
    indexY = 0
    for row in grid:
        maxY.append(max(row))
    for col in zip(*grid[::-1]):
        maxX.append(max(col))
    while indexX < len(col):
        while indexY < len(row):
            maxIncrease += (min(maxX[indexX], maxY[indexY]) - grid[indexX][indexY])
            indexY += 1
        indexX += 1
        indexY = 0
    return maxIncrease

def getMaxX(grid):
    maxX = []
    bufferList = []
    maxXGenCounter = 0
    while maxXGenCounter < len(grid):
        for row in grid:
            bufferList.append(row[maxXGenCounter])
            print (bufferList)
        maxXGenCounter += 1
        maxX.append(max(bufferList))
        bufferList = []
    print (maxX)

grid = [
    [3, 0, 8, 4], 
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]

print(solution(grid))
print(getMaxX(grid))