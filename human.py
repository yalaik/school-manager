from typing import Union
class Human:
    name: str
    last_name: str
    __id: Union[int, None]
    number_of_humans = 0
    collection_of_ids = set()

    def __init__(self, name, last_name, __id=None):
        self.name = name
        self.last_name = last_name
        Human.number_of_humans += 1
        if __id == None:
            __id = self.generate_id()
        else:
            if __id in Human.collection_of_ids:
                raise Exception("Переданный id уже существует!")
        self.__id = __id
        Human.collection_of_ids.add(__id)

    def generate_id(self):
        new_id = 1
        while new_id in Human.collection_of_ids:
            new_id += 1
        return new_id

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self):
        return f"Human(name={self.name}, last_name={self.last_name})"

    def __lt__(self, other: "Human"):
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name

    def __hash__(self):
        return hash(self.__id)

    def get_id(self) -> int:
        return self.__id