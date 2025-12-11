from abc import ABC, abstractmethod
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! Mp: {self.mp}"

class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"



class BankAccount:
    bank_name = "Simba"
    def __init__(self, hero, _balance, __password):
        self.hero = hero
        self._balance = _balance
        self.__password = __password


    def login(self, password):
        return password == self.__password

    def full_info(self):
        return (f"Банк: {self.bank_name}\n"
                f"Герой: {self.hero.name}\n"
                f"LVL: {self.hero.lvl}, HP = {self.hero.hp}\n"
                f"Баланс: {self._balance} Сом")

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return  f"{self.hero.name} | Баланс: {self._balance} Сом"

    def __add__(self, other):
        if type(self.hero) != type(other.hero):
            return f"Ошибка! Нельзя сложить баланс героев из разных классов!"
        return self._balance + other._balance

    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl



mage1 = MageHero("Garry", 80, 500, 150)
mage2 = MageHero("Garry", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 0)

acc1 = BankAccount(mage1, 5300, 1234)
acc2 = BankAccount(mage2, 8400, 0000)
acc3 = BankAccount(warrior, 3400, 4321)

print(mage1.action())
print(warrior.action())

print(acc1)
print(acc2)


print(f"Банк: {acc1.get_bank_name()}")
print(f"Бонус за уровень: {acc1.bonus_for_level()} Cом")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

print("\n=== Проверка __eq__ ===")

print("Mage1 == Mage2 ?", acc1 == acc2) # True — одинаковое имя и уровень

print("Mage1 == Warrior ?", acc1 == acc3)  # False



class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка _add_ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

print("Сумма мага и воина:", acc1 + acc3)

print("\n=== Проверка _eq_ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

sms = KGSms()
print("\n", sms.send_otp("+996777123456"))