from user import User

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def update_user(self, user_id, new_name, new_birthday, new_phone, new_email):
        for user in self.users:
            if user.get_id() == user_id:
                user.set_name(new_name)
                user.set_birthday(new_birthday)
                user.set_phone(new_phone)
                user.set_email(new_email)
                return True
        return False

    def remove_user(self, user):
        self.users.remove(user)

    def display_all_users(self):
        for user in self.users:
            user.display_info()
