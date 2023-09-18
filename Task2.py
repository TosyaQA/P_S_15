#Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.

#семинар 13 задача 2

import logging

logging.basicConfig(level=logging.DEBUG)

class InvalidNameError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NameDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            logging.error("ФИО должно начинаться с заглавной буквы и может содержать только буквы")
            raise InvalidNameError("ФИО должно начинаться с заглавной буквы и может содержать только буквы")
        setattr(instance, self._name, value)

class Student:
    last_name = NameDescriptor()
    first_name = NameDescriptor()
    middle_name = NameDescriptor()

    def __init__(self, last_name: str, first_name: str, middle_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        logging.info("Создан пользователь: " + self.last_name + ' ' + self.first_name + ' ' + self.middle_name)

    def print(self):
        print(self.last_name + ' ' + self.first_name + ' ' + self.middle_name)

try:
    s = Student('Иванов', 'Иван', 'Иванович')
    s.print()
except InvalidNameError as e:
    print(f"Ошибка создания студента: {str(e)}")

try:
    s = Student('иванов', 'И2ван', 'Иванович')
    s.print()
except InvalidNameError as e:
    print(f"Ошибка создания студента: {str(e)}")