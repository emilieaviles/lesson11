print('*' * 50)

print('Narrative Bot')

print()

name = input('Student Name: ')

grade = input('Student Grade: ')

grade = int(grade)

if grade >= 65: 
	grade = str(grade)
	print()
	print('Narrative:')
	print(name.capitalize() + ', your final grade in Computer Science is ' + grade + '%.')
	print('You have done well in all other components of the class.')
	print('You better keep it up next semester...or else...')
	print("You'll fail, duh.")

else: 
	grade = str(grade)
	print()
	print('Narrative:')
	print(name.capitalize() + ', your final grade in Computer Science is ' + grade + '%.')
	print('This is a result of a number of missed homework and classwork assignments.')
	print("Since your grade is lower than a 65, you'll have to complete a MBA next semester.")
print('*' * 50)