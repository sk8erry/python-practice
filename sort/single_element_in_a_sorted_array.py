'''LeetCode Problem
   Given a sorted array consisting of only integers where every element
   appears twice except for one element which appears once.
   Find this single element that appears only once.
   Note: Your solution should run in O(log n) time and O(1) space.'''

def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1: #Take care of 'list index out of range' error
            return nums[i]
        if nums[i] != nums[i+1]:
            return nums[i]

print (singleNonDuplicate([1,1,2]))
print (singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print (singleNonDuplicate([3,3,7,7,10,11,11]))
