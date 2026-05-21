class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):

        # Standard animal addition
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # Multiple animal addition using kwargs
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    def get_info(self):

        # Create farm header
        result = f"{self.name}'s farm\n\n"

        # Add animals and their counts
        for animal, count in self.animals.items():
            result += f"{animal}: {count}\n"

        # Add final farm sound
        result += "\n    E-I-E-I-0!"

        return result

    def get_animal_types(self):

        # Return sorted animal names
        return sorted(self.animals.keys())

    def get_short_info(self):

        # Get sorted animal list
        animals = self.get_animal_types()

        # Check if farm is empty
        if not animals:
            return f"{self.name} has no animals."

        sentence = f"The farm of {self.name} has "

        parts = []

        # Create plural or singular animal names
        for animal in animals:
            count = self.animals[animal]

            if count > 1:
                name = animal + "s"
            else:
                name = animal

            parts.append(name)

        # Return sentence for one animal
        if len(parts) == 1:
            return sentence + parts[0] + "."

        # Return sentence for multiple animals
        return sentence + ", ".join(parts[:-1]) + " and " + parts[-1] + "."

    def __str__(self):

        # String representation of the farm
        return f"Farm Name: {self.name}, Animals: {', '.join(self.animals)}"


# TEST
macdonald = Farm("McDonald")

macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)

print(macdonald.get_info())

print(macdonald.get_animal_types())

print(macdonald.get_short_info())

print(macdonald)