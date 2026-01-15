from productCollections import products
from categories import categories
from productPricing import prices

# Creating a list of products price and categories nested inside a tuple
# Using zip to combine products, prices and categories
# Creating a list of lists combining products, prices from dictionary, and categories
combined_operations = [
    [products[i], prices[i], categories[i]]
    for i in range(len(products))
]

print("Combined Operations (Product, Price, Category):")
print(tuple(combined_operations))

# Create a dictionary mapping each category to a list of product names
category_to_products = {}

for i, product in enumerate(products):
    category = categories[i]
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("\nCategory to Products Mapping:")
print(category_to_products)

# Create a reverse mapping - products to categories
product_to_categories = {}

for i, product in enumerate(products):
    category = categories[i]
    if product not in product_to_categories:
        product_to_categories[product] = []
    product_to_categories[product].append(category)

print("\nProduct to Categories Mapping:")
print(product_to_categories)

## Printing the products belonging to a specific category that has maximum products
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

print(f"\nCategory with maximum products: {max_category}")
print(f"Products in {max_category}: {category_to_products[max_category]}")