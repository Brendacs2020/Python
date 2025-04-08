n1 = float(input('Enter the first exam note: '))
n2 = float(input('Enter the second exam note: '))
average = (n1 + n2) / 2
if average < 5:
    print('You are reproved')
elif average > 6.9:
    print('You are aproved')
else:
    print('You are recuperation')
