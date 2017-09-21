'''Given an array of integers, return indices of the two numbers
   such that they add up to a specific target.
   You may assume that each input would have exactly one solution,
   and you may not use the same element twice.
   Example:
   Given nums = [2, 7, 11, 15], target = 9,
   Because nums[0] + nums[1] = 2 + 7 = 9,
   return [0, 1]. '''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    buffer_list = [''] * len(nums)
    for i in range(len(nums)):
        if (len(nums) == 0) or (len(nums) == 1):
            return None
        if target - nums[i] in buffer_list:
            return sorted([nums[i], target - nums[i]])
        else:
            buffer_list[i] = nums[i]

print(twoSum([1,2,3,4],6))
print(twoSum([1,2,3,4,5,6,45,6,7],51))
print(twoSum([1,4,6,7,4,3,4],1000))
