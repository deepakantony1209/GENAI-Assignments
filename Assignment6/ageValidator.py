def check_age(age):
    if age not in range(0, 121):
        raise Exception("Age must be between 0 and 120")
try:
    age = int(input("Enter you age:"))
    check_age(age)
except Exception as ve:
    print(ve)
else:
    print(f"Your age is {age}, you are eligible to proceed.")