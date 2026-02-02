# Reading the entire file with file.read()

with open('Assignment4/files/sales_data.txt', 'r') as file:
    print(file.read())

# Reading the first of file as file.lines()
with open('Assignment4/files/sales_data.txt', 'r') as file:
    print(file.readline())

# Read file and convert each line to integer
with open('Assignment4/files/sales_data.txt', 'r') as file:
    listOfIntegers = [int(line.strip()) for line in file.readlines()]
    print(listOfIntegers)

with open('Assignment4/files/sales_data.txt', 'r') as file:
    # file.readlines()
    print(type(file.readlines()))