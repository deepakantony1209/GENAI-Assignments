orders = [1200, 2500, 800, 1750, 3000]

if __name__ == "__main__":
    # Computing total amount after discount for a list of orders
    nodiscount = 0
    revenue = []

    # Iterating through each order amount to calculate discount and final amount
    for order in orders:
        if order >= 2000:
            discount = round(order * 0.15, 2)
        elif order in range(1500, 2000):
            discount = round(order * 0.10, 2)
        elif order in range(1000, 1500):
            discount = round(order * 0.07, 2)
        else:
            discount = 0
            nodiscount += 1

    # Printing order details and revenue
        print(f"Order Amount: {order}-> Discount: {discount}-> Final Amount to be paid: {order - discount + (order - discount)*0.05}")
        revenue.append(order - discount + (order - discount)*0.05)
        print("--------------------------------------------------")

    print("Total Revenue from all orders:", round(sum(revenue), 2))
    print("Number of orders with discount applied:", len(orders) - nodiscount)