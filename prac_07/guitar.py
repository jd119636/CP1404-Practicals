VINTAGE_REQUIREMENT = 50
CURRENT_YEAR = 2022

class Guitar:
    """Stores details about a Guitar"""

    def __init__(self, name = "", year = 0, cost = 0.0):
        """Initializes Guitar variables"""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Returns string representation of Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Returns age of Guitar based on the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if Guitar is Vintage"""
        return self.get_age() >= VINTAGE_REQUIREMENT


