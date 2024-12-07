class ClientShort:
    def __init__(self, name, surname, phone, id=None):
        if id is not None:
            self.set_id(id)
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

    # Валидация целого числа (неотрицательное)
    @staticmethod
    def validate_int(value):
        if not isinstance(value, int):
            return False  # Убедитесь, что значение - целое число
        if value < 0:
            return False  # Если сумма покупки отрицательная
        return True

    def set_id(self, id):
        if self.validate_int(id):
            self.id = id
        else:
            raise ValueError("ID не может быть отрицательным и должен быть целым числом.")

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

    def get_id(self):
        return getattr(self, 'id', None)  # Используем getattr, чтобы избежать AttributeError

    def get_phone(self):
        return self.phone

    # Строковое представление для вывода
    def __str__(self):
        return (f"ClientShort(id={self.get_id()}, name='{self.get_name()}', "
                f"surname='{self.get_surname()}', phone='{self.get_phone()}')")

    # Переопределение equals (сравнение объектов по телефону)
    def __eq__(self, other):
        if not isinstance(other, ClientShort):
            return False
        return self.phone == other.phone

    # Переопределение hashCode (хеш-код на основе телефона)
    def __hash__(self):
        return hash(self.phone)
