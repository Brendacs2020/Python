km = int(input('How long is your travel? '))
if km <= 200:
    print('Your travel cost R$ {} reias'.format(km * 0.50))
else:
    print('Your travel cost R$ {} reias'.format(km * 0.45))