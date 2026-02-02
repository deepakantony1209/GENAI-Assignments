from constructorEncapsulation import Product

class Laptop(Product):
    def __init__(self, name, price, category, brand, ram, storage):
        super().__init__(name, price, category)
        self.brand = brand
        self.ram = ram
        self.storage = storage
    
    def get_info(self):
        print(f"You have purchased a {self.brand} laptop with {self.ram} RAM and {self.storage} GB SSD Storage")
    
class Mobile(Product):
    def __init__(self, name, price, category, brand, model, storage):
        super().__init__(name, price, category)
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def get_info(self):
        print(f"You have purchased a {self.brand} {self.model}: {self.storage} GB Variant")

asus_tuf = Laptop("Asus TUF F15", "72000", "Gaming Laptop", "ASUS", "16GB", "512GB")
asus_tuf.get_info()
print(f"Total price: {asus_tuf.get_price()}")
print(f"Net price after discount: ", asus_tuf.apply_discount(15))
iphone_13 = Mobile("iPhone 13", "80000", "Smartphone", "Apple", "iPhone 13", "128GB")
iphone_13.get_info()    
print(f"Total price: {iphone_13.get_price()}")
print(f"Net price after discount: ", iphone_13.apply_discount(10))