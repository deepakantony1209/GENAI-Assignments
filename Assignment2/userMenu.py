from multipleOrderProcess import orders as order_amount
print("-----------------------------------------")
print("Press 1: Add order amount to running list")
print("Press 2: View all order amounts after applying discount")
print("Press q: Exit")
print("-----------------------------------------")

your_input = input("Enter your input:")
while your_input != "q":
    if your_input == "1":
        order_amount.append(float(input("Enter the order amount:")))
    elif your_input == "2":
        print("Order amounts with discount applied:")
        # Computing total amount after discount for a list of orders
        nodiscount = 0
        revenue = []
        # Iterating through each order amount to calculate discount and final amount
        for order in order_amount:
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
        print("Number of orders with discount applied:", len(order_amount) - nodiscount)
    else:
        print("Invalid input, please try again.")
        print("-----------------------------------------")
        print("Press 1: Add order amount to running list")
        print("Press 2: View all order amounts after applying discount")
        print("Press q: Exit")
        print("-----------------------------------------")
        your_input = input("Enter your input:")
        continue


    your_input = input("Enter your input:")

print("Thank you, have a great day!")

