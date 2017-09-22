def threeSum(nums, target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    buffer_list = [''] * len(nums)
    ansbuffer = []
    ans = []
    for i in range(len(nums)):
        buffer_list[i] = target - nums[i] #Create buffer list0
    for j in range(len(nums)):
        for k in range(len(nums)-1):
            running_list = nums[:k] + nums[k+1:]
            if (len(running_list) == 0):
                return None
            if (nums[j] + running_list[k] in buffer_list):
                if (len(set([nums.index(running_list[k]), j, \
                nums.index(target - nums[j] - running_list[k])])) == 3):
                    ansbuffer.append([nums[j], running_list[k], target - nums[j] - running_list[k]])
    ansbuffer = sorted(ansbuffer)
    if len(ansbuffer) == 1: return ansbuffer
    else:
        seen = set()
        for x in ansbuffer:
            x_set = frozenset(x)
            if x_set not in seen:
                ans.append(x)
                seen.add(x_set)
        return ans
print('answer is ', threeSum([3,-2,1,0],0))
print('answer is ', threeSum([6,4,7,3],17))
print('answer is ', threeSum([-2,1,1,3],0))
