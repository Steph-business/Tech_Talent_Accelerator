import math

# Daily Challenge: Pagination Class
class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        # page_num is 1-based
        if not isinstance(page_num, int) or page_num < 1 or page_num > self.total_pages:
            raise ValueError(
                f"Invalid page number. Must be between 1 and {self.total_pages}."
            )
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())


if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.get_visible_items())   # ['a', 'b', 'c', 'd']

    p.next_page()
    print(p.get_visible_items())   # ['e', 'f', 'g', 'h']

    p.last_page()
    print(p.get_visible_items())   # ['y', 'z']

    p.first_page()
    print(str(p))
    # a
    # b
    # c
    # d

    # Method chaining bonus
    p.first_page()
    print(p.next_page().next_page().next_page().get_visible_items())
    # ['m', 'n', 'o', 'p']

    # Error cases
    try:
        p.go_to_page(10)
    except ValueError as e:
        print(f"Caught: {e}")

    try:
        p.go_to_page(0)
    except ValueError as e:
        print(f"Caught: {e}")





# Daily Challenge Gold : DNA 
import random


class Gene:
    def __init__(self, value=None):
        self.value = random.randint(0, 1) if value is None else value

    def mutate(self):
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)


class Chromosome:
    def __init__(self, size=10):
        self.genes = [Gene() for _ in range(size)]

    def mutate(self):
        # each gene has a 1/2 chance to flip
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def is_all_ones(self):
        return all(g.value == 1 for g in self.genes)

    def __repr__(self):
        return "".join(repr(g) for g in self.genes)


class DNA:
    def __init__(self, size=10, chromosome_size=10):
        self.chromosomes = [Chromosome(chromosome_size) for _ in range(size)]

    def mutate(self):
        # each chromosome has a 1/2 chance to mutate
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_all_ones(self):
        return all(c.is_all_ones() for c in self.chromosomes)

    def __repr__(self):
        return " | ".join(repr(c) for c in self.chromosomes)


class Organism:
    def __init__(self, dna, environment):
        if not 0 <= environment <= 1:
            raise ValueError("environment must be a probability between 0 and 1")
        self.dna = dna
        self.environment = environment

    def live(self):
        # environment dictates the chance that the DNA mutates this generation
        if random.random() < self.environment:
            self.dna.mutate()

    @property
    def is_perfect(self):
        return self.dna.is_all_ones()


if __name__ == "__main__":
    # NOTE: full spec is 10 chromosomes x 10 genes = 100 bits.
    # Reaching all-ones by pure random mutation has probability (1/2)^100 ~ 1e-30
    # which is unobservable. We use a smaller DNA below to actually see a result.
    DNA_SIZE = 2
    CHROMOSOME_SIZE = 5         # 10 bits total -> ~1024 generations expected
    NUM_ORGANISMS = 100
    ENVIRONMENT = 0.9
    MAX_GENERATIONS = 1_000_000

    organisms = [
        Organism(DNA(DNA_SIZE, CHROMOSOME_SIZE), ENVIRONMENT)
        for _ in range(NUM_ORGANISMS)
    ]

    generation = 0
    winner = None
    while winner is None and generation < MAX_GENERATIONS:
        generation += 1
        for org in organisms:
            org.live()
            if org.is_perfect:
                winner = org
                break

    if winner:
        print(f"Perfect DNA reached after {generation} generations.")
        print(f"DNA: {winner.dna}")
    else:
        print(f"No perfect DNA after {MAX_GENERATIONS} generations.")