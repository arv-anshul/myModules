from functools import reduce
from factors import prime_factorisation


class Fraction:
    def __init__(self, numerator: int | float | str = 0, denominator: int = 1) -> None:
        """Module to perform Frations as in the form of `p/q`.
        ```python
        >>> Fraction(12.34)
        1234/100
        >>> Fraction('20/43')
        20/43
        ```

        Args:
            numerator (int | float | str, optional): Numerator of the Fraction. Defaults to 0.
            denominator (int, optional): Denominator of the Fraction. Defaults to 1.
        """
        # In case, numerator is string
        if isinstance(numerator, str):
            if len(numerator.split('/')) == 2:
                a, b = numerator.split('/')
                self.numerator, self.denominator = int(a), int(b)
            else:
                FractionException(
                    f'{numerator} form is not valid for string input. \nPlease provide string in the form of `p/q`.')

        # In case, numerator is float
        elif isinstance(numerator, float):
            self.numerator = int(''.join(str(numerator).split('.')))
            self.denominator = int(10 ** len(str(numerator).split('.')[1]))

            if denominator != 1 and denominator != 0:
                self.denominator *= denominator

        # In case, numerator is integer
        else:
            # In case, denominator is 0
            if denominator == 0:
                raise ZeroDivisionError()

            self.numerator = numerator
            self.denominator = denominator

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self) -> str:
        return f'Fraction({self.numerator}, {self.denominator})'

# Operators Magic Methods
    def __add__(self, other) -> object:
        temp_numerator = (self.numerator * other.denominator) + \
            (other.numerator * self.denominator)
        temp_denominator = self.denominator * other.denominator

        return Fraction(temp_numerator, temp_denominator).simplify()

    def __sub__(self, other) -> object:
        temp_numerator = (self.numerator * other.denominator) - \
            (other.numerator * self.denominator)
        temp_denominator = self.denominator * other.denominator
        return Fraction(temp_numerator, temp_denominator).simplify()

    def __mul__(self, other) -> object:
        temp_numerator = self.numerator * other.numerator
        temp_denominator = self.denominator * other.denominator
        return Fraction(temp_numerator, temp_denominator).simplify()

    def __truediv__(self, other) -> object:
        temp_numerator = self.numerator * other.denominator
        temp_denominator = self.denominator * other.numerator
        return Fraction(temp_numerator, temp_denominator).simplify()

    def __floordiv__(self, other) -> object:
        temp_numerator = self.numerator * other.denominator
        temp_denominator = self.denominator * other.numerator
        return Fraction(temp_numerator/temp_denominator).to_decimal()

    def __mod__(self, other):
        pass

    def __pow__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __eq__(self, other: object) -> bool:
        return True if self.numerator == other.numerator and self.denominator == other.denominator else False

    def __ne__(self, other: object) -> bool:
        return True if self.numerator != other.numerator or self.denominator != other.denominator else False

# int, str, float
# + - / * // == !=

    def simplify(self) -> object:
        # Check if numerator or denominator == 1
        if self.numerator == 1 or self.denominator == 1:
            return Fraction(self.numerator, self.denominator)

        nume_factors = prime_factorisation(self.numerator)
        deno_factors = prime_factorisation(self.denominator)

        # Taking {A-B as numerator} & {B-A as Denominator}.
        for i in nume_factors.copy():
            if i in deno_factors:
                nume_factors.remove(i)
                deno_factors.remove(i)

        # Creating simplified numerator and denominator variables
        simp_nume = reduce(lambda x, y: x*y, nume_factors)
        simp_deno = reduce(lambda x, y: x*y, deno_factors)

        return Fraction(simp_nume, simp_deno)

    def to_decimal(self):
        return self.numerator/self.denominator

    def _gcd(self, num1, num2):
        if num2 == 0:
            return num1
        return self._gcd(num2, num1 % num2)

    @staticmethod
    def reciprocal(fraction):
        return Fraction(fraction.denominator, fraction.numerator)


class FractionException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
