import re

class Client:
    def __init__(self, id, name, surname, patronymic, purchase_amount, phone, email):
        self.set_id(id)
        self.set_name(name)
        self.set_surname(surname)
        self.set_patronymic(patronymic)
        self.set_amount(purchase_amount)
        self.set_phone(phone)
        self.set_email(email)
        
    def __init__(self, client_data):
        data = client_data.split(',')
        if len(data) < 5:
            raise ValueError("Неверный формат данных. Ожидается минимум 5 значений.")

        # Разбираем строку, проверяя наличие значений
        if data[0].strip().isdigit():
            # Если первое значение - это id (число)
            self.id = int(data[0].strip())
            self.surname = data[1].strip()
            self.name = data[2].strip()
            self.patronymic = data[3].strip()

            if data[4].strip().isdigit():
                # Если следующее значение - это количество покупок (amount)
                self.amount = int(data[4].strip())
                self.phone = data[5].strip()
                self.email = data[6].strip()
            else:
                # Если значение для amount не передано
                self.amount = 0  # по умолчанию
                self.phone = data[4].strip()
                self.email = data[5].strip()
        else:
            # Если первое значение - это фамилия, а не id
            self.surname = data[0].strip()
            self.name = data[1].strip()
            self.patronymic = data[2].strip()

            if data[3].strip().isdigit():
                # Если следующее значение - это количество покупок (amount)
                self.amount = int(data[3].strip())
                self.phone = data[4].strip()
                self.email = data[5].strip()
            else:
                # Если значение для amount не передано
                self.amount = 0  # по умолчанию
                self.phone = data[3].strip()
                self.email = data[4].strip()


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def get_amount(self):
        return self.purchase_amount

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def set_id(self, id):
        self.id = self.validate_id(id)

    def set_name(self, name):
        self.name = self.validate_name(name)

    def set_surname(self, surname):
        self.surname = self.validate_surname(surname)

    def set_patronymic(self, patronymic):
        self.patronymic = self.validate_patronymic(patronymic)

    def set_amount(self, purchase_amount):
        self.purchase_amount = self.validate_amount(purchase_amount)

    def set_phone(self, phone):
        self.phone = self.validate_phone(phone)

    def set_email(self, email):
        self.email = self.validate_email(email)

    # Валидация ID
    @staticmethod
    def validate_id(id):
        if id <= 0:
            raise ValueError("ID должен быть положительным числом.")
        return id

    # Валидация имени
    @staticmethod
    def validate_name(name):
        if not name or not name.strip():
            raise ValueError("Имя не может быть пустым.")
        return name

    # Валидация фамилии
    @staticmethod
    def validate_surname(surname):
        if not surname or not surname.strip():
            raise ValueError("Фамилия не может быть пустой.")
        return surname

    # Валидация отчества
    @staticmethod
    def validate_patronymic(patronymic):
        if not patronymic or not patronymic.strip():
            raise ValueError("Отчество не может быть пустым.")
        return patronymic

    # Валидация суммы покупки
    @staticmethod
    def validate_amount(purchase_amount):
        if purchase_amount < 0:
            raise ValueError("Количество товаров не может быть отрицательным.")
        return purchase_amount

    # Валидация номера телефона
    @staticmethod
    def validate_phone(phone):
        if not phone or not phone.strip():
            raise ValueError("Номер телефона не может быть пустым.")
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise ValueError("Номер телефона должен содержать только цифры и может начинаться с +.")
        return phone

    # Валидация email
    @staticmethod
    def validate_email(email):
        if not email or not email.strip():
            raise ValueError("Email не может быть пустым.")
        if not re.match(r'^[A-Za-z0-9+_.-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})$', email):
            raise ValueError("Неверный формат email.")
        return email

    def __str__(self):
        return f"Client(id={self.id}, name='{self.name}', surname='{self.surname}', patronymic='{self.patronymic}', " \
               f"purchase_amount={self.purchase_amount}, phone='{self.phone}', email='{self.email}')"
