#This program to calculate the student's annual average (a1= 30%, a2 = 30% e a3= 40%)
a1 = float(input('Enter the a1 note: '))
a2 = float(input('Enter the a2 note: '))
a3 = float(input('Enter the a3 note: '))
avg = (a1 * 0.3 + a2 * 0.3 + a3 * 0.4)
print('The average is {:.2f}' .format(avg))
