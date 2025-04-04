year = int(input('What year do you want to analize? '))
if (year % 4) == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is leap year'.format(year))
else:
    print('{} is not leap year'.format(year))
