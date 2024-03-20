class   calculator:
    """Calculator"""

    def __init__(self, vector) -> None:
        self.vector = vector

    def __add__(self, object) -> None:
        """_summary_

        Args:
            object (_type_): _description_
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, object) -> None:
        """_summary_

        Args:
            object (_type_): _description_
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, object) -> None:
        """_summary_

        Args:
            object (_type_): _description_
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, object) -> None:
        """_summary_

        Args:
            object (_type_): _description_
        """
        try:
            if object == 0:
                raise AssertionError("Division by 0.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except AssertionError as e:
            print(f"Error: {e}")

