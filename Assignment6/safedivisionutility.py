try:
    num = int(input("Enter the Numerator: "))
    deno = int(input("Enter the Denominator: "))
    result = num/deno
except ValueError as exception1:
    print(exception1)
except ZeroDivisionError as exception2:
    print(exception2)
else:
    print(f"The division of {num}, {deno} is: ", result)
finally:
    print("Operation complete")
