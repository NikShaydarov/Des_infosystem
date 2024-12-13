class Client(ClientShort):
    def __init__(self, name, surname, phone,email, patronymic=None, purchase_amount=0, id=None):
        super().__init__(name, surname, phone, id=id)
        self.set_patronymic(patronymic)
        self.set_purchase_amount(purchase_amount)
        self.set_email(email)

    # Валидация отчества
    @staticmethod
    def validate_patronymic(patronymic):
        if patronymic is not None:
            if not patronymic or not patronymic.strip():
                return False
            if patronymic.isdigit():
                return False
        return True

    # Валидация суммы покупки
    @staticmethod
    def validate_purchase_amount(purchase_amount):
        if not isinstance(purchase_amount, (int, float)) or purchase_amount < 0:
            return False
        return True

    # Валидация email
    @staticmethod
    def validate_email(email):
        if not email or not email.strip():
            return False  # Email обязателен
        if not re.match(r'^[A-Za-z0-9+_.-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})$', email):
            return False
        return True

    def set_patronymic(self, patronymic):
        if self.validate_patronymic(patronymic):
            self.__patronymic = patronymic.strip() if patronymic else None
        else:
            raise ValueError("Отчество не может быть пустым, содержать только пробелы или быть числом.")

    def set_purchase_amount(self, purchase_amount):
        if self.validate_purchase_amount(purchase_amount):
            self.__purchase_amount = purchase_amount
        else:
            raise ValueError("Сумма покупки должна быть числом и не может быть отрицательной.")

    def set_email(self, email):
        if self.validate_email(email):
            self.__email = email.strip()
        else:
            raise ValueError("Неверный формат email.")

    def get_patronymic(self):
        return self.__patronymic

    def get_purchase_amount(self):
        return self.__purchase_amount

    def get_email(self):
        return self.__email

    # Строковое представление для вывода
    def __str__(self):
        return (f"Client(id={self.get_id()}, name='{self.get_name()}', surname='{self.get_surname()}', "
                f"patronymic='{self.get_patronymic()}', purchase_amount={self.get_purchase_amount()}, "
                f"phone='{self.get_phone()}', email='{self.get_email()}')")

    # Переопределение equals (сравнение объектов по телефону)
    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.__phone == other.__phone

    # Переопределение hashCode (хеш-код на основе телефона)
    def __hash__(self):
        return hash(self.__phone)
