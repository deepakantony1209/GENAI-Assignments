class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = int(price)
        self.category = category

    def get_info(self):
        print(f"From {self.category} you have purchased {self.name}.")

    def apply_discount(self, discount):
        return self.__price - (self.__price*(discount/100))    
    
    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = new_price
    
def update_price(product):
    user_choice = input(f"Do you want to update the price of product (yes/no): ")
    if user_choice.lower() == "yes":
        new_price = float(input("Enter the new price: "))
        product.set_price(new_price)
        print("Price updated successfully.")
    elif user_choice.lower() == "no":
        print("Price not updated.")
    else:
        raise ValueError("Invalid input. Please enter yes or no.")

if __name__ == "__main__":
    Pencil = Product("Pencil", "10", "Stationary")
    Pencil.get_info()
    print(f"Total price: {Pencil.get_price()}")
    print(f"Net price after discount: ", Pencil.apply_discount(10))
    update_price(Pencil)
    print(f"Total price: {Pencil.get_price()}")
    print(f"Net price after discount: ", Pencil.apply_discount(10))
    Eraser = Product("Eraser", "5", "Stationary")
    Eraser.get_info()
    print(f"Total price: {Eraser.get_price()}")
    print(f"Net price after discount: ", Eraser.apply_discount(10))
    update_price(Eraser)
    print(f"Total price: {Eraser.get_price()}")
    print(f"Net price after discount: ", Eraser.apply_discount(10))