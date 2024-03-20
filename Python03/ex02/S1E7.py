from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """_summary_
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        return super().die()

    def __str__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        return self.__str__()

class Lannister(Character):
    """Representing the Lannister family."""


    def __init__(self, first_name: str, is_alive: bool = True):
        """_summary_

        Args:
            first_name (str): _description_
            is_alive (bool, optional): _description_. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        return super().die()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """_summary_
        """
        x = cls(first_name, is_alive)
        return x

    def __str__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        return self.__str__()