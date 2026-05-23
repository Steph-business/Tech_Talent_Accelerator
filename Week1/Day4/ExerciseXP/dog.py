class Pets:

    def __init__(self, animals):
        self.animals = animals

    def walk(self):

        for animal in self.animals:
            print(animal.walk())


class Cat:

    is_lazy = True

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def walk(self):

        return f"{self.name} is just walking around"


class Bengal(Cat):

    def sing(self, sounds):
        return sounds


class Chartreux(Cat):

    def sing(self, sounds):
        return sounds


class Siamese(Cat):
    pass


# Création des objets
cat1 = Bengal("Milou", 5)
cat2 = Chartreux("Max", 3)
cat3 = Siamese("Rex", 2)


# Create list of all cats
all_cats = [cat1, cat2, cat3]


#  Create Pets object
sara_pets = Pets(all_cats)


# Walk all cats
sara_pets.walk()


# EXERCISE 2

# Create a class Dog 

class Dog :
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie "


    def run_speed(self):
        return self.weight / self.age * 10

    
    def fight(self, other_dog):
        power1 = self.run_speed() * self.weight
        power2 = other_dog.run_speed() * other_dog.weight

        if power1 > power2:
            return f"{self.name} wins the fight!" 

        else:
            return f"{other_dog.name} wins the fight!"


# Create 3 dogs

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 4, 25)

# Print the attributes of each dog
print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog1))




