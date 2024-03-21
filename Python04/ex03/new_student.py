import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    """_summary_
    """
    name: str = field(init=True)
    surname: str= field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.id = generate_id()
        self.login = self.name[0] + self.surname