"""
CP1404/CP5632 Practical - Suggested Solution
Basic manual tests for Guitar class
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2022


def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    new_guitar = Guitar("Another Guitar", 2013, 15000000.9)

    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{new_guitar.name} get_age() - Expected {9}. Got {new_guitar.get_age()}\n")

    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{new_guitar.name} is_vintage() - Expected {False}. Got {new_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()


