# Creating a list of products and a tuple for a sample product
products = ["Swift", "Baleno", "Punch", "Hyundai i20", "Kwid", "XUV 3XO"]
# print(products)
sample_product = ("Swift", 559000, "Hatchback")
# print(sample_product)

# Printing the second and last product from the products list
print(f"Second and last product: {products[-2:]}")
print(f"Second last product: {products[-2]}")
print(f"Last product: {products[-1]}")

# Appending two new products
products.append("Amaze")
products.append("Glanza")
print(products)

#Updating the tuple through type conversion and changing it back to tuple
converted_sample_product = list(sample_product)
converted_sample_product[1] = 649000
print(tuple(converted_sample_product))