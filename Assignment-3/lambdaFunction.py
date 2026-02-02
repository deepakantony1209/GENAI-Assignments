# GST Calculator using lambda function
gst_calculator = lambda price: price + (price * 0.18)
print("GST inclusive price:", gst_calculator(100))

# Final price after discount and GST using lambda function
final_price = lambda price, discount: price - price * (discount / 100) + ((price * (discount / 100)) * 0.18)
print("Final price after discount inclusive GST:", final_price(100, 10))

prices = [100, 250, 400, 1200, 50]

# Task 4: Apply GST to a list of prices using map
print(f"List of prices:{prices}")
gst_prices = list(map(gst_calculator, prices))
print(f"List of prices inclusive GST:{gst_prices}")

# Task 5: Filter Expensive products
# Function to check if price is greater than 500
def isExpensive(price):
    if price > 500:
        return True
    else:
        return False
# Function to check if price is less than or equal to 500    
def isLessThan500(price):
    if price <= 500:
        return True
    else:
        return False
    
expensive_prices = list(filter(isExpensive, gst_prices))
affordable_prices = list(filter(isLessThan500, gst_prices))

print(f"List of products (price > 500): {expensive_prices}")
print(f"List of products (price <= 500): {affordable_prices}")