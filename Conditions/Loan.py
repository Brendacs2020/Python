value = float(input('How much cost the house? '))
wage = float(input('How much do you get? '))
years = int(input('How many years will you pay? '))
time = years * 12
prestation = value / time

if (wage * 0.3) >= prestation:
    print('Congratulation, your loan is aproved and cost {:.2f}'.format(prestation))
else:
    print('Your loan is disaproved' )

