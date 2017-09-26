S = "1221121221221121122"

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
