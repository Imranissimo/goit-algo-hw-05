def caching_fibonacci():
    cache = {}

    def fibonacci(n: int):
        if n <= 0:
            cache[n] = 0
        elif n == 1:
            cache[n] = 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]
    
    return fibonacci

fib = caching_fibonacci()
