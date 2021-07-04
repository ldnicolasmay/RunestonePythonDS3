import random


class MSDie:
    """
    Mulit-sided die

    Instance variables:
        current_value
        num_sides
    """

    def __init__(self, num_sides) -> None:
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self) -> int:
        self.current_value = random.randrange(1, self.num_sides)
        return self.current_value

    def __str__(self) -> str:
        return str(self.current_value)

    def __repr__(self) -> str:
        return f"MSDie({self.num_sides} : {self.current_value})"

    def __eq__(self, other) -> bool:
        return self.current_value == other.current_value

    def __lt__(self, other) -> bool:
        return self.current_value < other.current_value

    def __le__(self, other) -> bool:
        return self.current_value <= other.current_value

