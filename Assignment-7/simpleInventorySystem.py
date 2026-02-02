class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} | Price: {self.price}"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        return NotImplemented

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]

    def get_total_value(self):
        return sum(p.price for p in self.products)

    def show_all_products(self):
        for p in self.products:
            print(p)

class Store(Inventory):
    def __init__(self, store_name):
        # FIX 1: Initialize the parent class so self.products exists
        super().__init__() 
        self.store_name = store_name

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        new_product = Product(name, price)
        self.add_product(new_product)

    def show_summary(self):
        print(f"\n--- {self.store_name} Summary ---")
        print(f"Total Items: {len(self.products)}")
        print(f"Total Value: {self.get_total_value()}")
        print("--------------------------")

# --- Testing the System ---

my_store = Store("Tech Junction")

# Adding 3 products
print("Adding items to inventory:")
for _ in range(3):
    my_store.add_new_product()

my_store.show_summary()

if len(my_store.products) >= 2:
    p1 = my_store.products[0]
    p2 = my_store.products[1]
    combined_price = p1 + p2
    print(f"Combined price of {p1.name} and {p2.name}: {combined_price}")