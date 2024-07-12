import unittest
from human import *
from student import *
from teacher import *
from subjects import *
from class_module import *



class TestSchoolManager(unittest.TestCase):

    def setUp(self):
        self.teacher1 = Teacher("Иван", "Иванов", [Subject.MATH, Subject.RUSSIAN_LANG])
        self.teacher2 = Teacher("Анна", "Смирнова", [Subject.FOREIGN_LANG])
        self.class_10A = Class(10, 'А', self.teacher1)
        self.student1 = Student("Имя3", "Фамилия3")
        self.student2 = Student("Имя1", "Фамилия1")
        self.student3 = Student("Имя4", "Фамилия4")
        self.student4 = Student("Имя2", "Фамилия2")
        self.student5 = Student('Имя5', 'Фамилия5')
        self.student6 = Student('Name0', 'Lastname0')

    def test_human_creation(self):
        human = Human("Тест", "Тестов")
        self.assertEqual(human.name, "Тест")
        self.assertEqual(human.last_name, "Тестов")

    def test_student_creation(self):
        student = Student("Имя", "Фамилия")
        self.assertEqual(student.name, "Имя")
        self.assertEqual(student.last_name, "Фамилия")

    def test_teacher_creation(self):
        teacher = Teacher("Учитель", "Учителев", [Subject.MATH])
        self.assertEqual(teacher.name, "Учитель")
        self.assertEqual(teacher.last_name, "Учителев")
        self.assertEqual(teacher._subjects, [Subject.MATH])

    def test_class_creation(self):
        self.assertEqual(self.class_10A.grade, 10)
        self.assertEqual(self.class_10A.letter, 'А')
        self.assertEqual(self.class_10A._homeroom_teacher, self.teacher1)

    def test_create_class_with_invalid_letter(self):
        with self.assertRaises(ValueError):
            Class(10, 'Z', self.teacher1)  #Буква дб А-Я

    def test_add_student(self):
        self.class_10A.add_student(self.student1)
        self.assertIn(self.student1, self.class_10A._students)
        self.assertEqual(self.student1.get_class(), self.class_10A)

    def test_remove_student(self):
        self.class_10A.add_student(self.student1)
        self.class_10A.remove_student(self.student1)
        self.assertNotIn(self.student1, self.class_10A._students)
        self.assertIsNone(self.student1.get_class())

    def test_write_read_csv(self):
        self.class_10A.add_student(self.student1)
        self.class_10A.add_student(self.student2)
        filename = 'class_test.csv'
        Class.write_csv(filename, self.class_10A)
        class_from_csv = Class.read_csv(filename)
        self.assertEqual(class_from_csv.grade, self.class_10A.grade)
        self.assertEqual(class_from_csv.letter, self.class_10A.letter)
        self.assertEqual(class_from_csv._homeroom_teacher.name, self.class_10A._homeroom_teacher.name)
        self.assertEqual(class_from_csv._homeroom_teacher.last_name, self.class_10A._homeroom_teacher.last_name)
        self.assertEqual(len(class_from_csv._students), len(self.class_10A._students))


if __name__ == '__main__':
    unittest.main()