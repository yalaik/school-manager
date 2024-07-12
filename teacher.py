from typing import Union, List
from human import Human
from subjects import Subject

class Teacher(Human):
    def __init__(self, name: str, last_name: str, subjects: List[Subject], homeroom_class: 'Class' = None, __id: Union[int, None] = None):
        super().__init__(name, last_name, __id)
        self._subjects = subjects
        self._homeroom_class = homeroom_class

    def set_class(self, homeroom_class: 'Class'):
        self._homeroom_class = homeroom_class

    def get_class(self) -> 'Class':
        return self._homeroom_class

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self):
        return f"Teacher(name={self.name}, last_name={self.last_name}, subjects={self._subjects})"