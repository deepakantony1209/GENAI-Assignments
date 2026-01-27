from constructorEncapsulation import Product, update_price

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.__warranty_years = warranty_years
    
    def get_info(self):
        print(f"From {self.category} you have purchased {self.name}.")
        return self.__warranty_years

calculator = ElectronicProduct("Calculator", "500", "Electronic Products", "2 Years")
print(f"This proudct includes {calculator.get_info()} warranty support")
print(f"Total price: {calculator.get_price()}")
print(f"Net price after discount: ", calculator.apply_discount(10))
update_price(calculator)
print(f"Total price: {calculator.get_price()}")
print(f"Net price after discount: ", calculator.apply_discount(10))