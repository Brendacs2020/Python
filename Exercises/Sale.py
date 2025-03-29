#This program calculate how much a sale item costs

originalcost = float(input('Enter the item value (R$): '))
discount = int(input('Enter the discount value (%): '))
print('The item cost {} with discount of {}%, it will cost {} reais'.format(originalcost, discount, originalcost - originalcost * (discount/100)))