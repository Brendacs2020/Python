#This prgram will convert the value in meter for centimeters and milimeters
m = float(input('Enter with a value in meters: '))
print('The value in centimeters is {:.2f} cm \nThe value in milimeters is {:.2f} mm' .format(m * 100, m * 1000))