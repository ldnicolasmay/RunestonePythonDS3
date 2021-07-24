from gcd import gcd


class Fraction:
    """
    Class Fraction
    """

    def __init__(self, top, bottom):
        """Constructor definition"""
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num:d}/{self.den:d}"

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        return self.num * other.den != other.num * self.den

    def __lt__(self, other):
        #  1     1
        # --- < ---
        #  3     2
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self.num * other.den <= other.num * self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self.num * other.den >= other.num * self.den

