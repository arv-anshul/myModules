def prime_factorisation(num):
    """Return a list of prime factors of given number.
    ```python
    >>> prime_factorisation(60)
    [2,2,3,5]
    ```

    Args:
        num (int): Number to factorize.

    Returns:
        list: Prime factors of given number.
    """
    factors = []

    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, (num // 2) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 2:
        factors.append(num)

    return factors
