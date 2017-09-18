#Given a string, return the longest substring without repeating characters

def longestSubstring(s):
    '''
    :type s: str
    :rtype: str
    '''
    running_str = ''
    running_longest = ''
    running_longer = ''
    for i in range(len(s)):
        if running_str.find(s[i-1]) == -1:
            print (s[i-1])
            running_str += s[i-1]
        else:
            if len(running_str) > len(running_longest):
                running_longest = running_str
            running_str = ''
            running_str += s[i-2]
            print(s[i-1])
    if len(running_longest) > len(running_str):
        return running_longest
    else:
        return running_str

print(longestSubstring('dvdf'))
