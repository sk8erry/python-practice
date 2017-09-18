def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        buff_string = str(x)
        if buff_string[0] == '-':
            return  int('-' + buff_string[:0:-1])
        else:
            return int(buff_string[::-1])

 #Test cases
print (reverse(-222), reverse(-12345), reverse(125645), reverse(0)) 
