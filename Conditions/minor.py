n1 = float(input('Enter a number: '))
n2 = float(input('Enter other number: '))
n3 = float(input('Enter other number: '))
if n1 < n2:
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
        print('{} is biggest number '.format(n3))