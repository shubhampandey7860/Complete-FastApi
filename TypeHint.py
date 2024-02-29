def Division(a: int, b: int) -> float:
    return a / b


print(Division(20, 10))


class Rectangle:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


r1 = Rectangle(2, 3)
print(r1.area())
