from typing import Union
from human import Human


class Student(Human):
    def __init__(self, name: str, last_name: str, student_class: 'Class' = None, __id: Union[int, None] = None):
        super().__init__(name, last_name, __id)
        self._class = student_class

    def set_class(self, student_class: 'Class'):
        self._class = student_class

    def get_class(self) -> 'Class':
        return self._class

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self):
        return f"{self.name} {self.last_name}"
#        return f"Student(name={self.name}, last_name={self.last_name})"