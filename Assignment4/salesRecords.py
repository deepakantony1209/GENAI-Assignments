sales = [1200, 450, 700, 3000, 150]

with open("Assignment4/files/sales_data.txt", "w") as f:
    for sale in sales:
        f.write(f"{sale}\n")

# Optional Writing a comma seperated version
with open("Assignment4/files/sales_data.txt", "w") as file:
    for i in range(len(sales)):
        if i == len(sales)-1:
            file.write(f"{sales[i]}.")
        else:
            file.write(f"{sales[i]}, ")