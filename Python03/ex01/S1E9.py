"""_summary_
ABC = Abstract Base Class
"""

from abc import ABC, abstractmethod

class   Character(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """_summary_

        Args:
            first_name (_type_): _description_
            is_alive (bool): _description_
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """_summary_
        """
        self.is_alive = False

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

class   Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        return super().die()

    def __str__(self) -> str:
        return f"Vector: ({self.first_name})"

    def __repr__(self) -> str:
        return self.__str__()