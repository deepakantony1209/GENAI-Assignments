# check for file name and handle FileNotFoundError and PermissionError
file_name = input("Enter the file name to read:")
try:
    with open(file_name, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")
else:
    with open(file_name, 'r') as file:
        # Read first three lines
        for content in range(3):
            line = file.readline()
            if line:
                print(line.strip())
            else:
                break
finally:
    print("File operation complete.")