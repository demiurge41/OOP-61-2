
class User:
    default_role = "guest"

    def __init__(self, username, role):
        self.username = username
        self.role = role


    def get_info(self):
        print(f"Пользователь: {self.username}, роль: {self.role}")


    @classmethod
    def create_guest(cls, username):
        return cls(username, cls.default_role)


    @staticmethod
    def is_admin(role):
        return role == "admin"


admin = User("Zara", "admin")
guest = User.create_guest("Chad")

admin.get_info()
guest.get_info()

print(User.is_admin(admin.role))
print(User.is_admin(guest.role))

