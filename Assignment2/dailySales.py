daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
for amount in daily:
    if amount == -1:
        print("Corrupted data encountered, stopping processing.")
        break
    elif amount == 0:
        print("No sales for the day.")
        continue
    else:
        print(f"Sales for the day: {amount}")
        total_sales += amount

print("Total sales processed:", total_sales)