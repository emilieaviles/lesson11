print('-' * 50)

print('Booze Bot')

print()

print("I'm a vending machine that dispenses different kinds of alcohol. Yay technology. Please answer the following question:")

print()

age = input('How old are you? ')

print()

age = int(age)

if age >= 21: 
	order = input('What would you like to order? ')
	print('Alrighty, cool guy. Please pay by swiping card on that flashing thing to the right. Pick up your ' + order.lower() + ' from the slot below.')

else: 
	years = 21 - age
	years = str(years)
	print("I think you're a bit too young to have alcohol. Come back in " + years + " years to order.")
print('-' * 50)