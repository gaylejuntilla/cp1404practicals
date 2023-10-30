"""Programming language Class"""


class ProgrammingLanguage:
    """Programming language class"""
    def __init__(self, field="", typing="", reflection=True, year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.field}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
