def is_perfect(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result == n
