

"""Reversing an array with 3 ways in python"""

def reversearray(a):
    a.reverse()
    return print(f'output of first way{a}')

def reversearray2(a):
    b = a[::-1]
    return print(f'output of second way{b}')

def reversearray3(a):
    """
    a combination of using iter and next object and
    """
    b = list(reversed(a))
    return print(f'output of third way{b}')


reversearray([1, 2, 3, 4])
reversearray2([1, 2, 3, 4])
reversearray3([1, 2, 3, 4])

