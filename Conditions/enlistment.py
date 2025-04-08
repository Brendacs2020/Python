from datetime import datetime

birth = str(input('Enter your birthday (ex:01/01/2000): '))
year = int(birth[6:10])
currentyear = datetime.now().year
if currentyear - year < 18:
    print('You must not enlist yet')
elif currentyear - year == 18:
    print('You must enlist')
else:
    print('You are past the deadline to enlist')