'''Given an array of 2n integers, your task is to group these integers
   into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn)
   which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

   Example 1:
   Input: [1,4,3,2]
   Output: 4

   Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
   Note:
   n is a positive integer, which is in the range of [1, 10000].
   All the integers in the array will be in the range of [-10000, 10000].'''
def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    ans = 0
    for i in range(0, len(nums), 2):
        ans += nums[i]
    return ans

print(arrayPairSum([1,3,2,4]))
print(arrayPairSum([1,4,7,3,6,78,3,5,234,56,6,45]))
print(arrayPairSum([6,8,3,7,34,8,23,67,9,10]))
