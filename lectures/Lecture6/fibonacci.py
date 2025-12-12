# fibonnacci.py

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 12
print(f"Here's the Fibonacci sequence from 0 to {n}:")
for i in range(n):
    print(f"Iteration {i}: {fibonacci(i)}")