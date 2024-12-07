class Client(ClientShort):
    def __init__(self, name, surname, phone, patronymic=None, purchase_amount=0, email=None, id=None):
        # Инициализация базового класса (ClientShort)
        super().__init__(name, surname, phone, id=id)
        self.set_patronymic(patronymic)
        self.set_purchase_amount(purchase_amount)
        self.set_email(email)

    # Сеттер для отчества с использованием валидации строки из ClientShort
    def set_patronymic(self, patronymic):
        if patronymic is None:
            self.patronymic = None
        elif self.validate_string(patronymic):
            self.patronymic = patronymic.strip()
        else:
            raise ValueError("Отчество не может быть пустым или содержать только пробелы.")

    # Валидация суммы покупки
    @staticmethod
    def validate_purchase_amount(value):
        if not isinstance(value, (int, float)):
            return False  # Убедитесь, что значение - число
        if value < 0:
            return False  # Если сумма покупки отрицательная
        return True

    # Сеттер для суммы покупки с вызовом валидации
    def set_purchase_amount(self, purchase_amount):
        if self.validate_purchase_amount(purchase_amount):
            self.purchase_amount = purchase_amount
        else:
            raise ValueError("Сумма покупок не может быть отрицательной и должна быть числом.")

    # Валидация email (отдельная функция)
    @staticmethod
    def validate_email(email):
        if not email or not email.strip():
            return False  # Если email пустой
        if not re.match(r'^[A-Za-z0-9+_.-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})$', email):
            return False  # Если email не соответствует формату
        return True

    # Сеттер для email с вызовом валидации
    def set_email(self, email):
        if email is None:
            self.email = None
        elif self.validate_email(email):
            self.email = email.strip()
        else:
            raise ValueError("Неверный формат email.")

    # Геттеры для дополнительных полей
    def get_patronymic(self):
        return self.patronymic

    def get_purchase_amount(self):
        return self.purchase_amount

    def get_email(self):
        return self.email

    # Метод для вывода информации о клиенте (короткий вариант)
    def str_short(self):
        return f"{self.name} {self.surname}"

    # Строковое представление для вывода полной информации о клиенте
    def __str__(self):
        return (f"Client(id={self.get_id()}, name='{self.get_name()}', surname='{self.get_surname()}', "
                f"patronymic='{self.get_patronymic()}', purchase_amount={self.get_purchase_amount()}, "
                f"phone='{self.get_phone()}', email='{self.get_email()}')")

    # Переопределение equals (сравнение объектов по телефону)
    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.phone == other.phone

    # Переопределение hashCode (хеш-код на основе телефона)
    def __hash__(self):
        return hash(self.phone)
