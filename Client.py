import re

class Client(ClientShort):
    def __init__(self, name, surname, phone, patronymic=None, purchase_amount=0, email=None):
        # Инициализация базового класса (ClientShort)
        super().__init__(name, surname, phone)
        
        self.set_patronymic(patronymic)
        self.set_purchase_amount(purchase_amount)
        self.set_email(email)

    # Сеттер для отчества с использованием валидации строки из ClientShort
    def set_patronymic(self, patronymic):
        if self.validate_string(patronymic):
            self.patronymic = patronymic.strip()
        else:
            raise ValueError("Отчество не может быть пустым или содержать только пробелы.")

    # Валидация суммы покупки
    @staticmethod
    def validate_purchase_amount(purchase_amount):
        if purchase_amount < 0:
            return False  # Если сумма покупки отрицательная
        return True

    # Сеттер для суммы покупки с вызовом валидации
    def set_purchase_amount(self, purchase_amount):
        if self.validate_purchase_amount(purchase_amount):
            self.purchase_amount = purchase_amount
        else:
            raise ValueError("Сумма покупок не может быть отрицательной.")

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
        if self.validate_email(email):
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
        return (f"Client(name='{self.name}', surname='{self.surname}', patronymic='{self.patronymic}', "
                f"purchase_amount={self.purchase_amount}, phone='{self.phone}', email='{self.email}')")
