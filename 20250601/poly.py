class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"({self.x}, {self.y})")

p1 = Point(1, 2)
p2 = Point(3, 4)

# p2 = Point(3, 4)
p3 = p1 + (3 , 4)
p3.display()  # Output: (4, 6)