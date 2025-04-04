speed = int(input('How fast was your car going when it passed the speed camera (Km/h)? '))
if speed <= 80:
    print('Congratulations! you were not fined!')
else:
    print('You have been fined')
    print('Your fine cost {},00 reais'.format((speed - 80) * 7))
