n = int(input())
if n == 1:
    print(2)
elif n == 0:
    print(0)
elif n % 2 == 0:
    print(int(((n / 2) + 1) * ((n / 2) + 1)))
else:
    m1 = (n - 1) / 2
    m2 = n - m1
    print(int((m1+1) * (m2+1)))
