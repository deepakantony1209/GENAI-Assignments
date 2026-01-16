prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percentage = int(input("Enter discount percentage: "))

with open("Assignment4/files/discounted_prices.txt", "w") as file:
    file.write("Product Name | Original Price | Discounted Price\n")
    for product, price in prices.items():
        discounted_price = price - (price * discount_percentage / 100)
        file.write(f"{product} | {price} | {discounted_price}\n")
    file.write(f"Average discounted price: {sum(prices.values())/len(prices)}")
    file.write(f"\nTotal items: {len(prices.values())}")

with open("Assignment4/files/discounted_prices.txt", "r") as file:
    print(file.read())