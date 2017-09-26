S = "1221121221221121122"

magical_string = [1,2,2]

for i in range(2,15):
    if i % 2 == 0:
        magical_string += [1] * magical_string[i]
    else:
        magical_string += [2] * magical_string[i]
print(magical_string)
