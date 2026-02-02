# Appending new sales values
with open("Assignment4/files/sales_data.txt", "a") as file:
    new_sales = [500, 2500, 1700]
    for sale in new_sales:
        file.write(f"{sale}\n")

# Reading updated Sales data
with open("Assignment4/files/sales_data.txt", "r") as file:
    print("Updated sales data:")
    print(file.read())

# Printing the total number of lines in files
with open("Assignment4/files/sales_data.txt", "r") as file:
    print(f"Total lines: {len(file.readlines())}.")