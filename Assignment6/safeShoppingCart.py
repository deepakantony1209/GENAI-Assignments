cart = []
nos_items = 0
user_input = ""
print("Enter 'q' to quit adding items to the cart.")
while user_input != "q":
    try:
        price = float(input(f"Enter price of item {nos_items+1}: "))
        if price < 0:
            raise Exception("Price cannot be negative")
        cart.append(price)
        nos_items += 1
        user_input = input("Press 'q' to quit or any other key to add item price:")
    except ValueError as ve:
        print("Invalid input. Please enter a numeric value for price.")
    except Exception as e:
        print(e)

print(f"Total items {len(cart)}")
print(f"Total price: {sum(cart)}")