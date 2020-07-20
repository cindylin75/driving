country = input('Where are you from:')
age = input('Please insert your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can take a driving license')
	else:
		print('you cannot take a driving license')
elif country == 'America':
	if age >= 16:
		print('You can take a driving license')
	else:
		print('you cannot take a driving license')
else:
		print('Please insert Taiwan/America')	