class Animal:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health

    def info(self):
        return f"{self.name}, {self.age} лет/года, здоровье {self.health}"

    def use_ability(self):
        return f"{self.name} использует базовую способность."

class Flyable:
    def use_ability(self):
        return super().use_ability() + " + Летает."

class Swimmable:
    def use_ability(self):
        return super().use_ability() + " + Плавает."

class Invisible:
    def use_ability(self):
        return super().use_ability() + " + Становится невидимым "




class Duck(Flyable, Swimmable, Animal):
    pass

class Bat(Flyable, Animal):
    pass

class Frog(Swimmable, Invisible, Animal):
    pass

class Phoenix(Flyable, Invisible, Animal):
    pass



class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_all(self):
        for animal in self.animals:
            print(animal.info())

    def perform_show(self):
        for animal in self.animals:
            print(animal.use_ability())

if __name__ == "__main__":
    zoo = Zoo()

    duck = Duck("Zigzag McQuack", 4, 90)
    bat = Bat("Bruce Wayne", 2, 100)
    frog = Frog("Tsarevna Lyagushka", 5,200)
    phoenix = Phoenix("Skyress Ventus", 9, 500)

    for animal in (duck, bat, frog, phoenix):
            zoo.add_animal(animal)

print("Информация о животных")
zoo.show_all()
print("\nШоу суперспособностей")
zoo.perform_show()

print("\nMRO для Duck:", Duck.__mro__)
print("MRO для Bat:", Bat.__mro__)
print("MRO для Frog:", Frog.__mro__)
print("MRO для Phoenix:", Phoenix.__mro__)