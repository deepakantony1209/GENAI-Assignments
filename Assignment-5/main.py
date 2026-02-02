# Importing math_utils in two ways and testing it

# Way 1

import math_utils
print(f"Addition with math_utils module: ", math_utils.add(100092930, 20930984))

# Way 2
from math_utils import square
print(f"Finding square of a number with math_utils module: ", square(12918237848172839871273))

# Importing string_utils and testing it

import string_utils
inputText = "Hello Dholakpur"
print(f"{inputText} in uppercase: {string_utils.capitalize_words(inputText)}")
print(f"{inputText} in reverse: {string_utils.reverse_string(inputText)}")
print(f"{inputText}'s word count: {string_utils.word_count(inputText)}")

# Importing shop_package here
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print("Welcome, Have a nice day:")
customer_years = int(input("Enter the number of years as a customer: "))
number_of_items = int(input("Enter the number of items you want to purchase: "))
item_prices = []
for i in range(number_of_items):
    price = float(input(f"Enter the price of item {i+1}: "))
    item_prices.append(price)

total = calculate_total(item_prices)

print("Total:", total)

if customer_years > 7:
    total = disc.apply_discount(total, 20)
    print(f"You are eligible for a 20% discount")
    print(f"Price after discount: {total}")
elif customer_years > 5:
    total = disc.apply_discount(total, 15)
    print(f"You are eligible for a 15% discount")
    print(f"Price after discount: {total}")
elif customer_years > 2:
    total = disc.apply_discount(total, 10)
    print(f"You are eligible for a 10% discount")
    print(f"Price after discount: {total}")
if customer_years == 0:
    total = disc.flat_discount(total)
    print(f"You are eligible for a flat 50 Rs. discount")
    print(f"Price after discount: {total}")

print(f"Total price after 5% tax: {apply_tax(total)}")