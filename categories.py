from productCollections import products

# Creating product categories for "products"
categories = ["Suzuki", "Suzuki", "Tata", "Hyundai", "Renault", "Mahindra", "Honda", "Toyota"]

# Converting it to set
categories_set = set(categories)
print(categories_set)

#Adding a new category
categories_set.add("Kia")
print("Categories set after adding a value:",categories_set)

#Trying to add a duplicate
categories_set.add("Honda")
print("Categoris after trying to add a duplicate value:",categories_set)

#Checking if a category is present
print("Tata" in categories_set)

# Printing total number of unique categories with set
print("Total unique categories:", len(categories_set))