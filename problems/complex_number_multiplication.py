'''Given two strings representing two complex numbers.
   You need to return a string representing their multiplication.
   Note: i^2 = -1 according to the definition.
   The input strings will not have extra blank.
   The input strings will be given in the form of a+bi, \
   where the integer a and b will both belong to the range of [-100, 100].
   And the output should be also in this form.'''

def complexNumberMultiply(a, b):
    """
        :type a: str
        :type b: str
        :rtype: str
    """
    element1 = a[:a.find('+')]
    element2 = a[a.find('+')+1:a.find('i')]
    element3 = b[:b.find('+')]
    element4 = b[b.find('+')+1:b.find('i')]
    e1, e2, e3, e4 = int(element1), int(element2), int(element3), int(element4)
    return(str(e1 * e3 + e2 * e4 * -1) + '+' + str((e1 * e4 + e2 * e3)) + 'i')


print(complexNumberMultiply('1+-1i','1+-1i'))
print(complexNumberMultiply('1+1i','1+-1i'))
print(complexNumberMultiply('5+7i','4+7i'))
