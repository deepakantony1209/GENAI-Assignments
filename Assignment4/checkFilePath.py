import os

# 1. Get the file name from the user
file_name = input("Enter the file name (e.g., example.txt): ")

# 2. Check if the file exists using os.path.isfile
# This checks if the path exists AND is a regular file
if os.path.isfile(file_name):
    print(f"Success! The file '{file_name}' is present in this directory.")
    print(f"Full path: {os.path.abspath(file_name)}")
else:
    # Check if file exists in current directory by listing files
    current_files = os.listdir(".")
    if file_name in current_files:
        print(f"The file '{file_name}' exists in the current directory.")
    else:
        print(f"The file '{file_name}' does not exist.")
        print(f"Current directory: {os.getcwd()}")
        print(f"Files in current directory: {current_files[:5]}...")  # Show first 5 files