with open("Assignment4/files/sales_data.txt", "r") as file:
    salesData = [int(line.strip()) for line in file.readlines()]
    print(f"Total sales: {sum(salesData)}")
    print(f"Highest sales: {max(salesData)}")
    print(f"Lowest sales: {min(salesData)}")
    print(f"Average sales: {sum(salesData)/len(salesData)}")