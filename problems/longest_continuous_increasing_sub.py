'''
Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
'''

def solution(nums):
    if len(nums) <= 1: return len(nums)
    start = 0
    end = 1
    length = 0
    while end < len(nums):
        if nums[end] > nums[end - 1]:
            end += 1
        else:
            start = end
            end += 1
        length = max(length, end - start)
    return length

print(solution([2,2,2,2,2]))