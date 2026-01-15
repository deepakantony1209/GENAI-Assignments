from productCollections import products

# Hardcoded prices for each product
prices = [559000, 679000, 549000, 699000, 379000, 859000, 599000, 699000]

# Create a dictionary using products list and prices
product_pricing = dict(zip(products, prices))

print("Product Pricing Dictionary:")
print(product_pricing)

# Adding new pair to the dictionary
product_pricing["Etios"] = 732000
print("Updated Product Pricing Dictionary:")
print(product_pricing)

# Removing a product from the dictionary using try-except
def remove_product(product_name):
    try:
        removed_product = product_pricing.pop(product_name)
        print("Removed Product:", removed_product)
        print(f"After removing {product_name}:", product_pricing)
    except KeyError:
        print("Removed Product: Product not found")

# Case 1: Product exists
remove_product("Punch")

# Case 2: Product does not exist
remove_product("Ciaz")

# Printing the average price of products in the dictionary
average_price = sum(product_pricing.values())/len(product_pricing)
print("Average Price of Products:", average_price)

# Finding the maximum priced product
maximum_priced_product = max(product_pricing.values())
for price in product_pricing:
    if product_pricing[price] == maximum_priced_product:
        max_product_name = price
print(f"The Highest priced car in the category is {maximum_priced_product}, {max_product_name}")

# Finding the minimum priced product
minimum_priced_product = min(product_pricing.values())
for price in product_pricing:
    if product_pricing[price] == minimum_priced_product:
        min_product_name = price
print(f"The Lowest priced car in the category is {minimum_priced_product}, {min_product_name}")