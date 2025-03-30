#This program caculates the new wage after rise

wage = int(input('Enter your current wage value (R$): '))
rise = int(input('Enter the rise value (%): '))
print('Your wage is {} with a rise of {}%, your wage will be {} reais'.format(wage, rise, wage + wage * (rise / 100)))