def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example
n_terms = 10
print(f"Fibonacci series up to {n_terms} terms: {fibonacci(n_terms)}")