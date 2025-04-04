from random import randrange

num = randrange(0,5)
choice = int(input('Choise a number tetween 0 and 5: '))
if num == choice:
    print('Congratulation, you got ir right')
else:
    print('Sorry, you are wrong, the correct number is', num)
