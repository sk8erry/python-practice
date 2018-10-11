'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''

def solution(digits):
    if len(digits) == 0: return digits
    flag = 1
    index = len(digits) - 1
    while (index >= 0) & (flag == 1):
        digits[index] = digits[index] + 1
        if digits[index] == 10:
            digits[index] = 0
            index = index - 1
        else: 
            flag = 0
    if index < 0: digits = [1] + digits
    return digits

print(solution([0]))
