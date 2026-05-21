
import random


# Exercise 1 & 2: Birthday look-up
birthdays = {
    'Alice': '1990/01/15',
    'Bob': '1985/05/30',
    'Carol': '1992/10/12',
    'Dave': '1978/07/04',
    'Eve': '2000/12/01'
}

def lookup_birthday():
    print("Welcome! You can look up birthdays of the people in the list.")
    # Exercise 2: print all names first
    print('Names:', ', '.join(birthdays.keys()))
    name = input('Enter a name: ').strip()
    bd = birthdays.get(name)
    if bd:
        print(f"{name}'s birthday is {bd}.")
    else:
        print(f"Sorry, we don't have the birthday information for {name}.")


# Exercise 3: Check the index of first occurrence
def check_index():
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
    name = input('Enter a name to check: ').strip()
    if name in names:
        print(names.index(name))
    else:
        print('Name not found')


# Exercise 4: Double Dice simulation
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


def main():
    # Run Birthday lookup (Exercises 1 & 2)
    lookup_birthday()
    print()
    # Run index check (Exercise 3)
    check_index()
    print()
    # Run doubles simulation (Exercise 4)
    simulate_doubles(100)


if __name__ == '__main__':
    main()
