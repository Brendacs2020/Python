#This program will sortition a studant

import random

s1 = str(input('Enter a name of first studant: '))
s2 = str(input('Enter a name of second studant: '))
s3 = str(input('Enter a name of thirst studant: '))
s4 = str(input('Enter a name of fourth studant: '))
list = [s1, s2, s3, s4]
print('The studant sorted is {}'.format(random.choice(list)))