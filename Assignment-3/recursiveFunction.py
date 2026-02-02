def factorial(n):
    if n < 0 and n != int(n):
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))