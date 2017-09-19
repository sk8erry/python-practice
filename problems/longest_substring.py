'''Given a string, return the longest substring without repeating characters'''

def longestSubstring(s):
    '''
    :type s: str
    :rtype: str
    '''
    running_str = ''
    running_longest = ''
    running_longer = ''
    i = 0
    counter = 0
    ifstuck = True
    while (i < len(s)):
        print (i)
        if running_str.find(s[i]) == -1:
            running_str += s[i]
        else:
            if len(running_str) > len(running_longest):
                running_longest = running_str
            running_str = ''
            i = i - 1
            running_str += s[i]
            ifstuck = not ifstuck 
            if ifstuck == True: break
        i += 1
        counter += 1
        #if counter > 10: break
    if len(running_longest) > len(running_str):
        return running_longest
    else:
        return running_str

print(longestSubstring('pwkew')) #output = vdf
print(longestSubstring('abcabcbb')) #output = abc
print(longestSubstring('dvdf')) #vdf
