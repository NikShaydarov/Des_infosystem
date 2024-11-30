import re

class ClientShort:
    def __init__(self, name, surname, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_phone(phone)

    # Валидация строки (не пустая и не состоит только из пробелов)
    @staticmethod
    def validate_string(value):
        if not value or not value.strip():
            return False  # Если строка пустая или состоит только из пробелов
        return True

    # Валидация номера телефона
    @staticmethod
    def validate_phone(phone):
        if not phone or not phone.strip():
            return False  # Если телефон пустой
        if not re.match(r'^\+?\d{10,15}$', phone):
            return False  # Если телефон не соответствует формату
        return True

    # Сеттер для имени с валидацией
    def set_name(self, name):
        if self.validate_string(name):
            self.name = name.strip()
        else:
            raise ValueError("Имя не может быть пустым или содержать только пробелы.")

    # Сеттер для фамилии с валидацией
    def set_surname(self, surname):
        if self.validate_string(surname):
            self.surname = surname.strip()
        else:
            raise ValueError("Фамилия не может быть пустой или содержать только пробелы.")

    # Сеттер для телефона с валидацией
    def set_phone(self, phone):
        if self.validate_phone(phone):
            self.phone = phone.strip()
        else:
            raise ValueError("Неверный формат телефона или пустое значение.")

    # Геттеры
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_phone(self):
        return self.phone

    # Строковое представление для вывода
    def __str__(self):
        return f"ClientShort(name='{self.name}', surname='{self.surname}', phone='{self.phone}')"
