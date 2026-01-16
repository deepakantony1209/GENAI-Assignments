# Creating an array of product name and prices
product_info = []
no_of_products = int(input("Enter number of products: "))

for i in range(no_of_products):
    name = input("Enter product name:")
    price = float(input("Enter product price:"))
    product_info.append([name, price])

with open("Assignment4/files/product_info.txt", "w") as file:
    file.write("Product Name | Price\n")
    for product in product_info:
        file.write(f"{product[0]} | {product[1]}\n")