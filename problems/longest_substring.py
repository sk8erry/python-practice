'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3
'''

def solution(str):
    if len(str) <= 1: return len(str)
    start = 0
    end = 1
    window = ''
    length = 0
    while end <= len(str) - 1:
        window = str[start:end]
        if str[end] not in window:
            end += 1
        else:
            start += 1
        length = max(length, end - start)
    return length

print(solution('abcabc'))
print(solution('au'))
print(solution('pwwkew'))


