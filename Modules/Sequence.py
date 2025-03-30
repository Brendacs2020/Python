#This program will sequence thes studants

import random

s1 = str(input('Enter a studant name: '))
s2 = str(input('Enter a studant name: '))
s3 = str(input('Enter a studant name: '))
s4 = str(input('Enter a studant name: '))
list = [s1, s2, s3, s4]
random.shuffle(list)
print('The apresentation sequence will be {}'.format(list))