n1 = float(input('Enter a number: '))
n2 = float(input('Enter other number: '))
n3 = float(input('Enter other number: '))
minor = n1
if n2<n1 and n2<n3:
    minor = n2
if n3<n1 and n3<n2:
    minor = n3

big = n1
if n2>n1 and n2>n3:
    big = n2
if n3>n1 and n3>n2:
    big = n3

print('{} is minor number '.format(minor))
print('{} is biggest number '.format(big))

'''if n1 < n2
    if n1 < n3:
        print('{} is minor number '.format(n1))
    else:
        print('{} is minor number '.format(n3))
else:
    if n2 < n3:
        print('{} is minor number '.format(n2))
    else:
        print('{} is minor number '.format(n3))
if n1 > n2:
    if n1 > n3:
        print('{} is biggest number '.format(n1))
    else:
        print('{} is biggest number '.format(n3))
else:
    if n2 > n3:
        print('{} is biggest number '.format(n2))
    else:
        print('{} is biggest number '.format(n3))'''