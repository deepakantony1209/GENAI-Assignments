from basicClass import Product

class MagicProduct(Product):
    def __str__(self):
        return f"Product(Name: {self.name}, Price: {self.get_price()}, Category: {self.category})"

    def __add__(self, other):
        return self.get_price() + other.get_price()

Obj1 = MagicProduct("Notebook", "50", "Stationary")
Obj2 = MagicProduct("Pen", "20", "Stationary")

print(Obj1)
print(Obj2)
print(f"Total price: {Obj1 + Obj2}")