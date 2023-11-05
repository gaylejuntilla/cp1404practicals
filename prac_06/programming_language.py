"""Programming language Class"""


class ProgrammingLanguage:
    """Programming language class"""
    def __init__(self, field="", typing="", reflection=True, year=0):
        """Initialise a Programming language object"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return boolean of whether language is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of data in a programming language"""
        return f"{self.field}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
