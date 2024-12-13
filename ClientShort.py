class ClientShort:
    def __init__(self, name, surname, phone, id=None):
        if id is not None:
            self.set_id(id)
        self.set_name(name)
        self.set_surname(surname)
        self.set_phone(phone)

    # Валидация имени (не пустое, не состоит только из пробелов, не число)
    @staticmethod
    def validate_name(name):
        if not name or not name.strip():
            return False
        if name.isdigit():
            return False
        return True

    # Валидация фамилии (не пустая, не состоит только из пробелов, не число)
    @staticmethod
    def validate_surname(surname):
        if not surname or not surname.strip():
            return False
        if surname.isdigit():
            return False
        return True

    # Валидация телефона
    @staticmethod
    def validate_phone(phone):
        if not phone or not phone.strip():
            return False
        if not re.match(r'^(?:\+7|8)(?:\d{10})$', phone):
            return False
        if not any(char.isdigit() for char in phone):
            return False
        return True

    # Валидация ID
    @staticmethod
    def validate_id(id):
        if not isinstance(id, int) or id < 0:
            return False
        return True


    def set_id(self, id):
        if self.validate_id(id):
            self.__id = id
        else:
            raise ValueError("ID должен быть целым числом и не отрицательным.")

    def set_name(self, name):
        if self.validate_name(name):
            self.__name = name.strip()
        else:
            raise ValueError("Имя не может быть пустым, содержать только пробелы или быть числом.")

    def set_surname(self, surname):
        if self.validate_surname(surname):
            self.__surname = surname.strip()
        else:
            raise ValueError("Фамилия не может быть пустой, содержать только пробелы или быть числом.")

    def set_phone(self, phone):
        if self.validate_phone(phone):
            self.__phone = phone.strip()
        else:
            raise ValueError("Неверный формат телефона или пустое значение.")

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_id(self):
        return getattr(self, '__id', None)

    def get_phone(self):
        return self.__phone

    # Строковое представление для вывода
    def __str__(self):
        return (f"ClientShort(id={self.get_id()}, name='{self.get_name()}', "
                f"surname='{self.get_surname()}', phone='{self.get_phone()}')")

    # Переопределение equals (сравнение объектов по телефону)
    def __eq__(self, other):
        if not isinstance(other, ClientShort):
            return False
        return self.get_phone() == other.get_phone()

    # Переопределение hashCode (хеш-код на основе телефона)
    def __hash__(self):
        return hash(self.get_phone())
