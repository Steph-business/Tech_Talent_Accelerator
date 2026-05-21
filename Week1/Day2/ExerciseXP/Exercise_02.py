
import random


# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_from_lists = dict(zip(keys, values))
print("Exercise 1:", dict_from_lists)


# Exercise 2: Cinemax #2 - calculate ticket prices for a family
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
def cinemax_total(family_dict):
	total = 0
	for name, age in family_dict.items():
		if age < 3:
			price = 0
		elif age <= 12:
			price = 10
		else:
			price = 15
		print(f"{name}: ${price}")
		total += price
	print("Total: $" + str(total))

print('\nExercise 2:')
cinemax_total(family)


# Exercise 3: Zara - create and modify a brand dictionary
brand = {
	'name': 'Zara',
	'creation_date': 1975,
	'creator_name': 'Amancio Ortega Gaona',
	'type_of_clothes': ['men', 'women', 'children', 'home'],
	'international_competitors': ['Gap', 'H&M', 'Benetton'],
	'number_stores': 7000,
	'major_color': {'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']}
}

brand['number_stores'] = 2
print('\nExercise 3:')
print('Clients:', ', '.join(brand['type_of_clothes']))
brand['country_creation'] = 'Spain'
if 'international_competitors' in brand:
	brand['international_competitors'].append('Desigual')
brand.pop('creation_date', None)
print('Last competitor:', brand['international_competitors'][-1])
print('US colors:', brand['major_color']['US'])
print('Number of keys:', len(brand))
print('Keys:', list(brand.keys()))


# Exercise 4: Describe a city and country (country has default)
def describe_city(city, country='Unknown'):
	print(f"{city} is in {country}.")

print('\nExercise 4:')
describe_city('Reykjavik', 'Iceland')
describe_city('Paris')


# Exercise 5: Random number compare
def compare_with_random(n):
	r = random.randint(1, 100)
	if n == r:
		print('Success!')
	else:
		print(f'Fail! Your number: {n}, Random number: {r}')

print('\nExercise 5:')
compare_with_random(50)  # example call


# Exercise 6: Make shirts with defaults and examples
def make_shirt(size='large', text='I love Python'):
	print(f'The size of the shirt is {size} and the text is {text}.')

print('\nExercise 6:')
make_shirt()
make_shirt('medium')
make_shirt(size='small', text='Custom message')


# Exercise 7: Temperature advice
def get_random_temp():
	return random.randint(-10, 40)

def main_temp():
	temp = get_random_temp()
	print(f"The temperature right now is {temp} degrees Celsius.")
	if temp < 0:
		print("Brrr, that's freezing! Wear extra layers.")
	elif temp <= 16:
		print("Quite chilly! Don't forget your coat.")
	elif temp <= 23:
		print("Nice weather.")
	elif temp <= 32:
		print("A bit warm, stay hydrated.")
	else:
		print("It's really hot! Stay cool.")

print('\nExercise 7:')
main_temp()


# Exercise 8: Pizza toppings loop
def pizza_order():
	toppings = []
	while True:
		t = input("Enter a topping (or 'quit' to finish): ").strip()
		if t.lower() == 'quit':
			break
		if t:
			print(f"Adding {t} to your pizza.")
			toppings.append(t)
	base = 10.0
	total = base + 2.5 * len(toppings)
	print('Toppings:', toppings)
	print(f'Total price: ${total:.2f}')


def birthday_lookup():
	birthdays = {
		'Alice': '1990/01/15',
		'Bob': '1985/05/30',
		'Carol': '1992/10/12',
		'Dave': '1978/07/04',
		'Eve': '2000/12/01'
	}
	print('\nBirthday Exercise:')
	print('Available names:', ', '.join(birthdays.keys()))
	name = input('Enter a name: ').strip()
	bd = birthdays.get(name)
	if bd:
		print(f"{name}'s birthday is {bd}.")
	else:
		print(f"Sorry, we don't have the birthday information for {name}.")


def check_index():
	names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
	name = input('Enter a name to check: ').strip()
	if name in names:
		print(names.index(name))
	else:
		print('Name not found')


def throw_dice():
	return random.randint(1, 6)


def throw_until_doubles():
	count = 0
	while True:
		count += 1
		a = throw_dice()
		b = throw_dice()
		if a == b:
			return count


def simulate_doubles(trials=100):
	results = []
	for _ in range(trials):
		results.append(throw_until_doubles())
	total_throws = sum(results)
	average = total_throws / len(results)
	print(f'Total throws: {total_throws}')
	print(f'Average throws to reach doubles: {average:.2f}')

if __name__ == '__main__':
	print('\nExercise 8:')
	pizza_order()
	print()
	birthday_lookup()
	print()
	check_index()
	print()
	simulate_doubles(100)
