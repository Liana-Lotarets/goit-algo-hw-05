# Create a function caching_fibonacci().
def caching_fibonacci():
    # Create an empty dictionary.
    cache = dict()
    # Create a function fibonacci()
    def fibonacci(n: int) -> int:
        # First Fibonacci number is equal to 0.
        if n <= 0:
            return 0
        # Second Fibonacci number is equal to 1.
        elif n == 1:
            return 1
        # Maybe the number has already saved in dictionary "cache".
        elif n in cache:
            return cache[n]
        # Calculate n-th Fibonacci number.
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # Return n-th Fibonacci number.
        return cache[n]
    # Return the function fibonacci.
    return fibonacci


# Get the function fibonacci
fib = caching_fibonacci()

# Use the function fibonacci for calculating Fibonacci numbers.
print(fib(10))
print(fib(15))
print(fib(5))
