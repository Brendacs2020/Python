#This program calculates the sine, cosine and tangent

import math 

num = float(input('Enter a number: '))
print('The angle {}° has sine of {:.2f}, cosine of {:.2f} and tangent of {:.2f}'.format(num, math.sin(math.radians(num)), math.cos(math.radians(num)), math.tan(math.radians(num))))