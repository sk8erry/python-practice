'''
Example 1:
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.

Example 2:
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.
'''

def findPoisonedDuration(timeSeries, duration):
    if len(timeSeries) <= 1: return duration * len(timeSeries)
    poisonedDuration = 0
    index = 1
    while index < len(timeSeries):
        if timeSeries[index] - timeSeries[index - 1] <= duration:
            poisonedDuration += timeSeries[index] - timeSeries[index - 1]
            index += 1
        else:
            poisonedDuration += duration
            index += 1
    poisonedDuration += duration
    return poisonedDuration

print(findPoisonedDuration([1,2,3,4,5,6,7,8,9],1))