# Класс должен иметь любое название на ваш выбор (например: Car, Cat, Phone, Student, Pizza,
# GameCharacter, Laptop и т.д.)

#В __init__ должно быть минимум 3 атрибута (передаётся через параметры)
#Должно быть минимум 2 своих метода (кроме __init__)

#В конце файла создайте минимум 2–3 объекта этого класса и вызовите
# у них методы (чтобы было видно, что всё работает)

class Pizza:

   def __init__(self, name, size, toppings):
       self.name = name
       self.size = size
       self.toppings = toppings
       self.baked = False

   def bake(self):
       if not self.baked:
           self.baked = True
           return f"Пицца {self.name} - готова!"
       return f"Пицца {self.name} - e;t "

   def add_topping(self, topping):
       self.toppings.appened(topping)
       return f"Добавлена начинка {topping}!"

   def info(self):
       status = "готова" if self.baked else "ещё готовится"
       return f"Пицца '{self.name}', размер {self.size} см, начинки: {', '.join(self.toppings)}. Статус: {status}."


# Создаём несколько котов и проверяем
pizza1 = Pizza("Маргарита", 30, ["сыр", "томаты"])
pizza2 = Pizza("Пепперони", 35, ["сыр", "пепперони"])
pizza3 = Pizza("Гавайская", 25, ["сыр", "ананас", "курица"])


print(pizza1.info())
print(pizza1.bake())
print(pizza1.add_topping("пикули"))
print(pizza1.info())

print("\n" + pizza2.info())
print(pizza2.add_topping("соус терияки"))
print(pizza2.bake())

print("\n" + pizza3.info())
print(pizza3.bake())

