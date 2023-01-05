""" A module to perform the rational operations. """


from typing import Self


class Fraction:
    """ This class perform fraction operations in rational form as p/q. """

    def __init__(self, numerator: int | float = 0, denominator: int | float = 1):
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
        if denominator == 0:
            raise FractionException('Denominator cannot be 0.')
        elif isinstance(numerator, str) or isinstance(denominator, str):
            raise FractionException(
                'Numerator or Denominator must be a float or a integer.')

        if isinstance(numerator, float):
            fr = Fraction.from_decimal(numerator)
            self.__p = fr.Numerator
            self.__q = fr.Denominator
        elif isinstance(numerator, int):
            hcf = self.__hcf(numerator, denominator)
            self.__p = Fraction.__filter_float(numerator // hcf)
            self.__q = Fraction.__filter_float(denominator // hcf)

    def __str__(self) -> str:
        if self.__q == 1:
            return str(self.__p)
        elif self.__p > 0 and self.__q < 0:
            return f'-{self.__p}/{abs(self.__q)}'
        elif self.__p < 0 and self.__q < 0:
            return f'{abs(self.__p)}/{abs(self.__q)}'
        else:
            return f'{self.__p}/{self.__q}'

    def __repr__(self) -> str:
        return f'Fraction({self.__p}, {self.__q})'

    @property
    def Numerator(self) -> float:
        """ Return the Numerator of fraction. """
        return self.__p

    @Numerator.setter
    def Numerator(self, value: int | float) -> None:
        """ Setter for the Numerator of fraction. """
        if isinstance(value, (int, float)):
            self.__p = value

    @property
    def Denominator(self) -> float:
        """ Return the Denominator of fraction. """
        return self.__q

    @Denominator.setter
    def Denominator(self, value: int | float) -> None:
        """ Setter for the Denominator of fraction. """
        if isinstance(value, (int, float)):
            self.__q = value

    def __add__(self, other: Self | float) -> Self:
        if isinstance(other, Fraction):
            temp_p = ((self.__p * other.__q) + (other.__p * self.__q))
            temp_q = ((self.__q * other.__q) /
                      Fraction.__hcf(self.__p, self.__q))
            return Fraction(temp_p, temp_q)
        else:
            return Fraction(self.todecimal_ + other * self.Denominator, self.Denominator)

    def __sub__(self, other: Self | float) -> Self:
        if isinstance(other, Fraction):
            return self + other.negative_
        else:
            return Fraction(self.Numerator - other * self.Denominator, self.Denominator)

    def __mul__(self, other: Self | float) -> Self:
        if isinstance(other, Fraction):
            temp_p = self.__p * other.__p
            temp_q = ((self.__q * other.__q) /
                      Fraction.__hcf(self.__p, self.__q))
            return Fraction(temp_p, temp_q)
        else:
            return Fraction(self.Numerator * other, self.Denominator)

    def __floordiv__(self, other: Self | float) -> float:
        if isinstance(other, Fraction):
            return (self * other.reciprocal_).todecimal_
        else:
            return self.todecimal_ * (1/other)

    def __truediv__(self, other: Self | float) -> Self:
        if isinstance(other, Fraction):
            return self * other.reciprocal_
        else:
            return Fraction(self.Numerator, self.Denominator * other)

    def __pow__(self, other: Self | float) -> Self | None:
        if isinstance(other, Fraction):
            if self.todecimal_ < 0 and (other.todecimal_ % 2 == 0 or 2 % other.todecimal_ == 0):
                return None
            else:
                temp_p = self.__p ** round(other.todecimal_, 2)
                temp_q = self.__q ** round(other.todecimal_, 2)
                return Fraction(temp_p, temp_q)
        else:
            return Fraction(self.__p**other, self.__q**other)

    def __eq__(self, other: Self | float) -> bool:
        if isinstance(other, Fraction):
            return True if self.__p == other.__p and self.__q == other.__q else False
        else:
            return True if self.todecimal_ == other else False

    def __ne__(self, other: Self | float) -> bool:
        return False if self == other else True

    def __lt__(self, other: Self | float) -> bool:
        if isinstance(other, Fraction):
            return True if self.todecimal_ < other.todecimal_ else False
        else:
            return True if self.todecimal_ < other else False

    def __gt__(self, other: Self | float) -> bool:
        return False if self < other else True

    def __le__(self, other: Self | float) -> bool:
        return True if self < other or self == other else False

    def __ge__(self, other: Self | float) -> bool:
        return True if self > other or self == other else False

    @staticmethod
    def __hcf(a: int | float, b: int | float) -> int | float:
        if b == 0:
            return a
        return Fraction.__hcf(b, a % b)

    @property
    def reciprocal_(self) -> Self:
        """ Return the reciprocal value of the fraction."""
        return Fraction(self.__q, self.__p)

    @property
    def negative_(self) -> Self:
        """ Return the negative value of the fraction."""
        return Fraction(-self.__p, self.__q)

    @property
    def todecimal_(self) -> float:
        """ Return the decimal value of the fraction."""
        return self.__p / self.__q

    @classmethod
    def from_decimal(cls, decimal: float) -> Self:
        """Used for converting decimal values to fraction object.
        ```python
        >>> Fraction.from_decimal(12.3)
        Fraction(123, 10)

        Args:
            decimal (float): Decimal value to convert into fraction object.

        Returns:
            Fraction: Fraction object.
        """
        if isinstance(decimal, (int, float)):
            p, q = str(float(decimal)).split('.')
            len_q = len(q)
            return Fraction(int(p+q), 10**len_q)

    @staticmethod
    def __filter_float(x: int | float) -> int | float:
        """Remove point value if float is 14.0 to 14.

        Args:
            x (int | float): A float value.

        Returns:
            int | float: Filtered value if float is 14.0 to 14.
        """
        if isinstance(x, int):
            return x
        if isinstance(x, float):
            a, b = str(x).split('.')
            if b == '0':
                return int(a)
            else:
                return x


class FractionException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
