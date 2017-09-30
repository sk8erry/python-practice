'''A magical string S consists of only '1' and '2' and obeys the following rules:
   The string S is magical because concatenating the number of contiguous
   occurrences of characters '1' and '2' generates the string S itself.
   The first few elements of string S is the following:
   S = "1221121221221121122……"
   If we group the consecutive '1's and '2's in S, it will be:
   1 22 11 2 1 22 1 22 11 2 11 22 ......
   and the occurrences of '1's or '2's in each group are:
   1 2 2 1 1 2 1 2 2 1 2 2 ......
   You can see that the occurrence sequence above is the S itself.
   Given an integer N as input, return the number of '1's in the
   first N number in the magical string S.

   Note: N will not exceed 100,000.'''

def count1sInMagicalString(n):
    magical_string = [1,2,2]
    counter = 0
    if n == 0: return 0
    for i in range(2, n):
        if i % 2 == 0:
            magical_string += [1] * magical_string[i]
        else:
            magical_string += [2] * magical_string[i]
        if magical_string[i] == 1: counter += 1
    return counter + 1

print(count1sInMagicalString(5),count1sInMagicalString(10),count1sInMagicalString(1))
