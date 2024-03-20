"""_summary_
ABC = Abstract Base Class
"""

from abc import ABC, abstractmethod

class   Character(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
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
        pass

class   Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
