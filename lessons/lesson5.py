# 2. Метод класса (@classmethod)
class User:
    # Атрибуты класса (имеет одинаковое значение для всех экз класса)
    default_role = "guest"

    def __init__(self, username, role:str = 'n/a'):
        # Атрибуты экземпляра класса (зависят от самого экз класса [self.username = username])
        self.username = username
        self.role = role

    @classmethod
    def create_from_name(cls, username):
        return cls(username, cls.default_role)


    @classmethod
    def get_base_role(cls):
        return cls.default_role

    def get_name(self):
        return  self.username

zara = User("Zara", "Admin")

print(zara.get_name())

# print(User.get_base_role()) #guest












