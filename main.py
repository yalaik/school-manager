from human import *
from student import *
from teacher import *
from subjects import *
from class_module import *

# Примеры использования

# Создание учителей с предметами
teacher1 = Teacher("Иван", "Иванов", [Subject.MATH, Subject.RUSSIAN_LANG])
teacher2 = Teacher("Анна", "Смирнова", [Subject.FOREIGN_LANG])

# Создание класса
class_10A = Class(1, 'А', teacher1)

# Создание студентов
student1 = Student("Имя3", "Фамилия3",None, 7)
student2 = Student("Имя1", "Фамилия1")
student3 = Student("Имя4", "Фамилия4")
student4 = Student('Имя2', 'Фамилия2')
student5 = Student('Имя5', 'Фамилия5')
student6 = Student('Name0', 'Lastname0')

# Добавление студентов в класс
class_10A.add_student(student1)
class_10A.add_student(student2)
class_10A.add_student(student3)
class_10A.add_student(student4)
class_10A.add_student(student5)
class_10A.add_student(student6)

# Примеры работы с классом
print(class_10A)
print("Ученики, начинающиеся на 'Им':", class_10A['Им'])
for student in class_10A:
    print(student)

# print(student1 < student3)
# print("ПетровМаксим" < "ПетровМаксин")

# print(f"Всего инициировано {Human.number_of_humans} человек(а)")
# print(Human.collection_of_ids)

# Запись класса в CSV
Class.write_csv('class_10A.csv', class_10A)

# Чтение класса из CSV
class_from_csv = Class.read_csv('class_10A.csv')
print(class_from_csv)
for student in class_10A:
    print(student)
