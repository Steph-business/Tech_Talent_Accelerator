import math
import random

# EXERCISE XP 

# Exercise 1: Cat Class
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Whiskers", 2)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 3)


def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1

    if cat2.age > oldest_cat.age:
        oldest_cat = cat2

    if cat3.age > oldest_cat.age:
        oldest_cat = cat3

    return oldest_cat

# Get the oldest cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")


# Exercise 2: Dog Class

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Buddy", 40)

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")

else:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")




# Exercise 3: Song Class

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# create song object

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
    ])

stairway.sing_me_a_song()



# Exercise 4: Zoo Class

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        self.grouped_animals = grouped_animals
        return grouped_animals

    def get_grouped_animals(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Create a zoo object
brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal(
    "Giraffe",
    "Bear",
    "Baboon",
    "Lion",
    "Zebra",
    "Cat",
    "Cougar"
    )

print("Animals in the zoo:")

brooklyn_safari.get_animals()
print()

print("Grouped animals in the zoo:")
brooklyn_safari.get_grouped_animals()





# Exercise XP GOLD

# Exercise 1: Geometry Class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("A circle is a round shape where all points are at the same distance from the center.")

circle1 = Circle(5)
print(f"Area: {circle1.area()}")
print(f"Perimeter: {circle1.perimeter()}")
circle1.definition()




# Exercise 2: Custom List Class
class MyList:
    def __init__(self):
        self.letters = []

    def reverse_list(self):
        return self.letters[::-1]

    def sort_list(self):
        return sorted(self.letters)

    def random_number(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]

# Test the MyList class
my_list = MyList()
my_list.letters = ['b', 'a', 'c', 'd']
print(f"Original list: {my_list.letters}")
print(f"Reversed list: {my_list.reverse_list()}")
print(f"Sorted list: {my_list.sort_list()}")
print(f"Random numbers: {my_list.random_number()}")


# Exercise 3: Restaurant Menu Manager Class

class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        new_item = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_item)
        print(f"Added {name} to the menu.")

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                print(f"Updated {name} on the menu.")
                return
        print(f"{name} not found on the menu.")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"Removed {name} from the menu.")
                return
        print(f"{name} not found on the menu.")

# Test
manager = MenuManager()
manager.add_item("Pizza", 20, "B", True)
manager.update_item("Soup", 20, "A", False)
manager.remove_item("Salad")
print("\nFinal Menu:\n")
for item in manager.menu:
    print(item)


# EXERCISE XP NINJA


class Phone:
    def __init__(self, phone_number):

        # Store phone number
        self.phone_number = phone_number

        # Store call history
        self.call_history = []

        # Store messages
        self.messages = []

    # Make a phone call
    def call(self, other_phone):

        message = f"{self.phone_number} called {other_phone.phone_number}"

        print(message)

        # Save call in both phones history
        self.call_history.append(message)
        other_phone.call_history.append(message)

    # Display call history
    def show_call_history(self):

        print(f"\nCall history for {self.phone_number}:")

        for call in self.call_history:
            print(call)

    # Send message
    def send_message(self, other_phone, content):

        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }

        # Save message in both phones
        self.messages.append(message)
        other_phone.messages.append(message)

        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")

    # Show sent messages
    def show_outgoing_messages(self):

        print(f"\nOutgoing messages from {self.phone_number}:")

        for message in self.messages:

            if message["from"] == self.phone_number:
                print(message)

    # Show received messages
    def show_incoming_messages(self):

        print(f"\nIncoming messages for {self.phone_number}:")

        for message in self.messages:

            if message["to"] == self.phone_number:
                print(message)

    # Show messages from a specific phone number
    def show_messages_from(self, number):

        print(f"\nMessages from {number}:")

        for message in self.messages:

            if message["from"] == number:
                print(message)


# TEST
phone1 = Phone("0707070707")
phone2 = Phone("0101010101")
phone3 = Phone("0505050505")

# Calls
phone1.call(phone2)
phone2.call(phone3)

# Show call history
phone1.show_call_history()
phone2.show_call_history()

# Send messages
phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi!")
phone3.send_message(phone1, "Good morning!")

# Show outgoing messages
phone1.show_outgoing_messages()

# Show incoming messages
phone1.show_incoming_messages()

# Show messages from specific number
phone1.show_messages_from("0505050505")