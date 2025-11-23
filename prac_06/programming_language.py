class ProgrammingLanguage:
    """Represents information about a given programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing}, Reflection ={self.reflection}, First appeared in {self.year}\n"

    def is_dynamic(self):
        """Determine if the language is dynamic."""
        return self.typing == "Dynamic"


