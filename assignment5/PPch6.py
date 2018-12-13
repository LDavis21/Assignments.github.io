print(-2.8)
print(abs(-4.3))
print(34.5)

import calendar
print(calendar)


def average(num1, num2):
    """(number, number) -> number

    Return the average of num1 and num2

    average(10, 20)
    15.0
    average(2.5, 3.0)
    2.75
    """
    return num1 + num2 / 2

import doctest
doctest.testmod()
