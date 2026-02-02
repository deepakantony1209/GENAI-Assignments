prices = [120, 350, 'abc', 500, -200, 800]
total = 0
for price in prices:
    try:
        total+=price
        if price < 0:
             raise Exception("Negative value found")
    except TypeError as te:
        print(f"{price} is not a number, rejecting this for price calculation")
    except Exception as ne:
            print(f"{price} is in Negative. Negative values aren't allowed.")
    else:
        print(total)