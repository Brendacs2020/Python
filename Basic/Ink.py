#This program calculate the area with based in width and length. So, calcule how much ink is necessary.

width = float(input('Enter the width (meters) wall: '))
length = float(input('Enter the length (meters) wall: '))
print('The wall is {} m² and it will take {} liters to paint it '.format(width * length, (width * length) / 2))
