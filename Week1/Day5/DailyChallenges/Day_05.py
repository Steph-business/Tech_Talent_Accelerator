# Daily challenge Gold - Circle

import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if (radius is None) == (diameter is None):
            raise ValueError("Provide exactly one of radius or diameter")
        self.radius = radius if radius is not None else diameter / 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius


if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=20)
    c3 = Circle(radius=3)

    print(c1)
    print(c2)
    print(c3)

    # __add__
    c4 = c1 + c3
    print(f"c1 + c3 = {c4}")

    # __eq__ and __gt__
    print(f"c1 == c3: {c1 == c3}")
    print(f"c2 > c1:  {c2 > c1}")

    # Sorting uses __lt__
    circles = [c1, c2, c3, c4]
    circles.sort()
    print("Sorted (smallest -> largest):")
    for c in circles:
        print(f"  {c}")



# Daily Challenge : Challenge 



#Challenge 1 — Draw Circles
import turtle

def draw_circles(circles):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    y = -200
    for c in sorted(circles):
        t.penup()
        t.goto(0, y)
        t.pendown()
        t.circle(c.radius * 10)  # scale x10 for visibility
        y += c.diameter * 10 + 10
    screen.mainloop()


#Challenge 2 — Longest Word
def longest_word(sentence):
    return max(sentence.split(), key=len)

    if _name_ == "_main_":

        print(longest_word("Margaret's toy is a pretty doll."))
        
        # Margaret's
        print(longest_word("A thing of beauty is a joy forever."))

        # forever.
        print(longest_word("Forgetfulness is by all means powerless!"))
        

