import collections

barchasb = list(input())
tekrar = collections.Counter(barchasb)
if tekrar['R'] >= 3:
    print('nakhor lite')
elif tekrar['R'] >= 2 and tekrar['Y'] >= 2:
    print('nakhor lite')
elif tekrar['G'] == 0:
    print('nakhor lite')
else:
    print('rahat baash')