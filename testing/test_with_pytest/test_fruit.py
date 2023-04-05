import pytest
from typing import List


class Fruit():
    def __init__(self, name: str) -> None:
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad():
    def __init__(self, *fruit_bowl: List[str]) -> None:
        self.fruit = fruit_bowl
        self._cube_fruit = self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


@pytest.fixture
def fruit_bowl():
    return [Fruit("Apple"), Fruit("Banana")]


def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


# Request other fixtures #
@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def second_entry():
    return "a"


@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]
