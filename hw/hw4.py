class Product:
    def __init__(self, title: str, price: int, quantity: int):
        self.title = title
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product(title="{self.title}", price={self.price}, quantity={self.quantity})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.price < other.price

    def __add__(self, other):
        return Product(
            "Combo",
            self.price + other.price,
            1
        )


p1 = Product("Клавиатура", 1500, 10)
p2 = Product("Клавиатура", 1800, 5)
p3 = Product("Мышка", 700, 20)

print(p1 == p2)
print(p3 < p1)

combo = p1 + p3
print(combo)