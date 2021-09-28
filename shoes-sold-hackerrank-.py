import collections

v1 = int(input("shoe number\n"))
v2 = list(map(int, input("space seprated shoe sizes\n").strip().split()))
v2 = collections.Counter(v2)
print(v2)
print(f"{v2} is the available shoe sizes")
v3 = int(input("customers\n"))
print(f"{v3} is the count of customers")
sumofsold = 0
for i in range(1, v3 + 1):
    voroodi = list(map(int, input().strip().split()))
    if voroodi[0] in v2 and v2[voroodi[0]] > 0:
        print(voroodi)
        print(f"first in {i} count of size is  {v2[voroodi[0]]}")
        sumofsold += voroodi[1]
        v2[voroodi[0]] = v2[voroodi[0]]-1
        print(f"second in {i} count of size is  {v2[voroodi[0]]}")
        print(f"sum is {sumofsold}")
    else:
        print(f"size {voroodi[0]} not available")
print(sumofsold)

