num = int(input('Enter a number: '))
choice = int(input('1 for binary \n2 for octal \n3 for hexadecimal \nChoice a number conform the menu bellow: '))
if choice == 1:
    print('{} in binary is {}'.format(num, bin(num)))
if choice == 2:
    print('{} in octal is {}'.format(num, oct(num)))
if choice == 3:
    print('{} in hexadecimal is {}'.format(num, hex(num)))