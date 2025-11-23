"""Band class – holds a list of musicians and manages the band."""

class Band:
    """Represent a band composed of multiple musicians."""

    def __init__(self, name: str):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        musician_list = "\n  ".join(str(musician) for musician in self.musicians)
        return f"{self.name} band:\n  {musician_list}"

    def play(self):
        """Make each musician play their instruments."""
        if not self.musicians:
            return f"{self.name} has no musicians!"
        # Each musician has a play() method that returns a string
        return "\n".join(musician.play() for musician in self.musicians)
