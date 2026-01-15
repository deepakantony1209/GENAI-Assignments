order_amount = float(input("Enter the order amount:"))
if order_amount >= 2000:
    discount = order_amount * 0.15
elif order_amount in range(1500, 2000):
    discount = order_amount * 0.10
elif order_amount in range(1000, 1500):
    discount = order_amount * 0.07
else:
    discount = 0

print("Your order Amount:", order_amount)
print("Discount:", discount)
sub_total = order_amount - discount
print("Subtotal:", sub_total)
tax = sub_total * 0.05
print("Tax", tax)
print("Total amount to be paid:", sub_total+tax)