def weeks_elapsed(day1, day2):
    """(int, int) -> int
    
    Return the number of full weeks that have ellapsed between the two days.

    weeks_elapsed(3, 20)
    2
    weeks_elapsed(20, 3)
    2
    weeks_elapsed(8, 5)

    weeks_elasped(40, 61)
    """
    return int(abs((day1 - day2) / 7))

print()


def square(num):
    """(number) -> number
    Return the square of num.

    square(3)
    9
    """
    return num ** 2

print()
