
class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return a string representation of Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of guitar from current year"""
        return 2023 - self.year

    def is_vintage(self):
        """Determine if guitar is vintage if it is >= 50 years old"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Determine if guitar is newer"""
        return self.year < other.year
