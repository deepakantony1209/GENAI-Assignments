# Function definition
def apply_discount(price, percentage=5):
    percentage = percentage / 100  # Convert percentage to decimal
    if percentage < 0 or percentage > 1:
        raise ValueError("Percentage must be between 0 and 1.")
    elif percentage > 0.6:
        raise ValueError("Percentage cannot be greater than 60%.")
    else:
        return price * (1 - percentage)
    
# Calling function
final_price = apply_discount(100, 20)
print(f"Final price after discount: {final_price}")

# Calling function with default percentage
final_price_default = apply_discount(100)
print(f"Final price after default discount: {final_price_default}")

# Calling function with invalid percentage
try:
    final_price_invalid = apply_discount(100, 70)
except ValueError as e:
    print(e)