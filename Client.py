class Client:
    def __init__(self, id, name, surname, patronymic, purchase_amount, phone, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.purchase_amount = purchase_amount
        self.phone = phone
        self.email = email

    # Геттеры и сеттеры
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_patronymic(self):
        return self.patronymic

    def set_patronymic(self, patronymic):
        self.patronymic = patronymic

    def get_purchase_amount(self):
        return self.purchase_amount

    def set_purchase_amount(self, purchase_amount):
        self.purchase_amount = purchase_amount

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"Client(id={self.id}, name='{self.name}', surname='{self.surname}', patronymic='{self.patronymic}', " \
               f"purchase_amount={self.purchase_amount}, phone='{self.phone}', email='{self.email}')"
