class User:
    def __init__(self, id, name, birthday, phone, email):
        self._id = id
        self._name = name
        self._birthday = birthday
        self._phone = phone
        self._email = email

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_birthday(self):
        return self._birthday

    def set_birthday(self, value):
        self._birthday = value

    def get_phone(self):
        return self._phone

    def set_phone(self, value):
        self._phone = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def display_info(self):
        print(f"User Information:")
        print(f"ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Birthday: {self.get_birthday()}")
        print(f"Phone: {self.get_phone()}")
        print(f"Email: {self.get_email()}")
