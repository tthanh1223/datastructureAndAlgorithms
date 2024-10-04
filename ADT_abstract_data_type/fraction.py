from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise ValueError("Both numerator and denominator must be integers.")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def get_num(self):
        return self.numerator

    def get_den(self):
        return self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction(numerator={self.numerator}, denominator={self.denominator})"

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __radd__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.denominator + self.numerator, self.denominator)
        return NotImplemented

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)
    def __rmul__(self, other):
        if isinstance(other, int):
            if gcd(self.denominator, other) == 1:
                return Fraction(other*self.numerator, self.denominator)
            else:
                return Fraction(self.numerator*other//gcd(self.denominator, self.numerator),self.denominator//gcd(self.denominator, self.numerator))
        return NotImplemented

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __iadd__(self, other):
        if isinstance(other, Fraction):
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator
        elif isinstance(other, int):
            self.numerator += other * self.denominator
        else:
            return NotImplemented

        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        return self
def test_fraction_class():
    # Test creation of fractions
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = Fraction(5, 2)  # Should raise ValueError for denominator = 0
    try:
        f3 = Fraction(5, 0)
    except ValueError as e:
        print(e)

    # Test string representation
    print(str(f1))  # Expected: 1/2
    print(repr(f1))  # Expected: Fraction(numerator=1, denominator=2)

    # Test addition
    f4 = f1 + f2
    print(f"{f1} + {f2} = {f4}")  # Expected: 1/2 + 3/4 = 5/4

    # Test right addition
    f5 = 2 + f1
    print(f"2 + {f1} = {f5}")  # Expected: 2 + 1/2 = 5/2

    # Test in-place addition
    f1 += f2
    print(f"f1 after f1 += f2: {f1}")  # Expected: 5/4

    # Test subtraction
    f6 = f1 - f2
    print(f"{f1} - {f2} = {f6}")  # Expected: 5/4 - 3/4 = 1/4

    # Test multiplication
    f7 = f1 * f2
    print(f"{f1} * {f2} = {f7}")  # Expected: 5/4 * 3/4 = 15/16

    # Test division
    f8 = f1 / f2
    print(f"{f1} / {f2} = {f8}")  # Expected: 5/4 / 3/4 = 5/3

    # Test relational operators
    print(f"{f1} > {f2}: {f1 > f2}")  # Expected: True
    print(f"{f1} < {f2}: {f1 < f2}")  # Expected: False
    print(f"{f1} == {f2}: {f1 == f2}")  # Expected: False
    print(f"{f1} != {f2}: {f1 != f2}")  # Expected: True

    # Test negative fractions
    f9 = Fraction(-1, 2)
    f10 = Fraction(1, -2)
    print(f"{f9} == {f10}: {f9 == f10}")  # Expected: True

    # Test mixed operations
    f11 = f1 + f2 - f9 * 2
    print(f"{f1} + {f2} - {f9} * 2 = {f11}")  # Expected: Complex result based on previous fractions

# Run the test cases
test_fraction_class()
f5 = Fraction(5, 2)
print(4*f5)