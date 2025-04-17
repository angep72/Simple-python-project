# Create a function that uses recursion to find the nth Fibonacci number.
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
