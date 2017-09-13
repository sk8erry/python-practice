#你获得了一串数字（奇数个位数），需要对数字进行解密
#解密规则是这样的：首先将第1个数删除，紧接着将第2个数放到这串数的末尾
#再将第3个数删除并第4个数放到这串数的末尾
#如此重复，直到剩下最后一个数，将这个数也删除
#按照刚才删除的顺序，把这些删除的数连在一起就是明码了

import math

def decode(array,deleted):
    if len(array) > 1:
        for i in range(2):           
            deleted.append(array.pop(0))
            array.append(array.pop(0)) 
        return decode(array,deleted)       
    else:
        return deleted + array

code = [6,3,1,7,5,8,9,2,4]
decoded = []
print("The answer is",decode(code,decoded))