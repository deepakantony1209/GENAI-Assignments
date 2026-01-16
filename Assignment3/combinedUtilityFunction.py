# Combined utility function that applies a 10% discount to a list of prices and filters those above 300
def process_prices(prices):
    apply_discount = lambda price: price - (price * 0.1)
    discounted_prices = list(map(apply_discount, prices))
    def above300(price):
        if price > 300:
            return True
        else:
            return False
    discounted_prices_above_300 = list(filter(above300, discounted_prices))
    return discounted_prices, discounted_prices_above_300

# Example usage
x,y = process_prices([100, 500, 900, 50, 750])
print(f"Prices inclusive 10% discount:{x}")
print(f"Prices higher than 300 after 10% discount:{y}")