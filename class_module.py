import csv
from typing import List
from teacher import Teacher
from student import Student
from human import Human
from subjects import Subject


class Class:
    #_grade: int
    #_letter: str
    #_students: List["Student"]
    #_homeroom_teacher: "Teacher"
    Cyrillic_Capital_Letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def __init__(self, grade: int, letter: str, homeroom_teacher: Teacher, students: List[Student] = None):
        self.grade = grade # Будет использован сеттер для проверки
        self.letter = letter # Будет использован сеттер для проверки
        self._students = students if students else []
        self._homeroom_teacher = homeroom_teacher

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if isinstance(value, int) and 1 <= value <= 11:
            self._grade = value
        else:
            raise ValueError("Цифра должна быть числом 1-11")

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, value):
        if len(value) == 1 and value.isupper() and value in self.Cyrillic_Capital_Letters:
           self._letter = value
        else:
            raise ValueError("Буква дб А-Я")


    def __getitem__(self, name: str) -> List[Student]:
        return [student for student in self._students if student.name.startswith(name) or
                student.last_name.startswith(name)]

    def __iter__(self):
        return iter(sorted(self._students, key=lambda student: (student.last_name, student.name)))

    def add_student(self, student: Student):
        self._students.append(student)
        student.set_class(self)

    def remove_student(self, student: Student):
        self._students.remove(student)
        student.set_class(None)

    def __str__(self):
        return f"{self._grade}{self._letter} класс, классный руководитель: {self._homeroom_teacher}"

    def __repr__(self):
        return (f"Class(grade={self._grade}, letter={self._letter}, homeroom_teacher={self._homeroom_teacher}, "
                f"students={self._students})")

    @staticmethod
    def write_csv(filename: str, class_instance: 'Class'):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Grade', 'Letter', 'Teacher_Name', 'Teacher_Last_Name', 'Subjects'])
            writer.writerow([class_instance._grade, class_instance._letter,
                             class_instance._homeroom_teacher.name, class_instance._homeroom_teacher.last_name,
                             ','.join([subject.name for subject in class_instance._homeroom_teacher._subjects])])
            writer.writerow([])
            writer.writerow(['ID', 'Student_Name', 'Student_Last_Name'])
            for student in class_instance._students:
                writer.writerow([student.get_id(), student.name, student.last_name])

    @staticmethod
    def read_csv(filename: str):
        Human.collection_of_ids.clear()
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            grade, letter = int(rows[1][0]), rows[1][1]
            teacher_name, teacher_last_name = rows[1][2], rows[1][3]
            subjects = [Subject[subject] for subject in rows[1][4].split(',')]
            teacher = Teacher(teacher_name, teacher_last_name, subjects)
            students = []
            for row in rows[4:]:
                _id, name, last_name = int(row[0]), row[1], row[2]
                students.append(Student(name, last_name, None, _id))
            class_instance = Class(grade, letter, teacher, students)
            for student in students:
                student.set_class(class_instance)
            return class_instance
