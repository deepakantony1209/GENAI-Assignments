class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = int(price)
        self.category = category

    def get_price(self):
        return self.price
    
    def get_info(self):
        print(f"From {self.category} you have purchased {self.name}.")
        print(f"Total price: {self.price}")

    def apply_discount(self, discount):
        return self.price - (self.price*(discount/100))    
    
def __main__():
    Pencil = Product("Pencil", "10", "Stationary")
    Pencil.get_info()
    print(f"Net price after discount: ", Pencil.apply_discount(10))
    Eraser = Product("Eraser", "5", "Stationary")
    Eraser.get_info()
    print(f"Net price after discount: ", Eraser.apply_discount(10))
