

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


def reversearray4(a):
    start = 0
    end = len(a)-1
    while start < end:
        temp = a[start]
        a[start] = a[end]
        a[end] = temp
        start += 1
        end -= 1
    return print(f'output of 4th way{a}')

reversearray([1, 2, 3, 4])
reversearray2([1, 2, 3, 4])
reversearray3([1, 2, 3, 4])
reversearray4([1, 2, 3, 4])

