import re

class Client:
    def __init__(self, name, surname, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_phone(phone)

    # Валидация строки (не пустая и не состоит только из пробелов)
    @staticmethod
    def validate_string(value):
        if not value or not value.strip():
            raise ValueError("Строка не может быть пустой или содержать только пробелы.")
        return value.strip()

    # Валидация номера телефона
    @staticmethod
    def validate_phone(phone):
        if not phone or not phone.strip():
            raise ValueError("Номер телефона не может быть пустым.")
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise ValueError("Номер телефона должен содержать только цифры и может начинаться с +.")
        return phone

    # Сеттер для имени с валидацией
    def set_name(self, name):
        self.name = self.validate_string(name)

    # Сеттер для фамилии с валидацией
    def set_surname(self, surname):
        self.surname = self.validate_string(surname)

    # Сеттер для телефона с валидацией
    def set_phone(self, phone):
        self.phone = self.validate_phone(phone)

    # Геттеры
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_phone(self):
        return self.phone

    # Метод для вывода информации о клиенте
    def __str__(self):
        return f"Client(name='{self.name}', surname='{self.surname}', phone='{self.phone}')"
