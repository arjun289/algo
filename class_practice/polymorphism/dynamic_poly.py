"""
Dynamic polymorphism is when a function implemented by the base
class is overriden by a child class.
"""


class Animal():
    def __init__(self) -> None:
        pass

    def print_animal(self):
        description = "I am from the Animal class"
        print(f"{description}")

    def print_animal_2(self):
        description = "I am from the Animal class"
        print(f"{description}")


class Lion(Animal):
    def __init__(self) -> None:
        super()

    def print_animal(self):
        description = "I am from the lion class"
        print(description)


if __name__ == "__main__":
    lion = Lion()
    lion.print_animal()
    lion.print_animal_2()
