'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''

def solution(height):
    if len(height)==2: return min(height[0], height[1])
    indexL = 0
    indexR = len(height) - 1
    maxArea = 0
    while True:
        currentArea = (indexR - indexL) * min(height[indexL], height[indexR])
        maxArea = max(currentArea, maxArea)
        print(indexL, indexR)
        if height[indexL] > height[indexR]: indexR -= 1
        elif height[indexL] <= height[indexR]: indexL += 1
        if indexL == indexR: break
    return maxArea

height = [1,2,1]
print(solution(height))