def is_prime(n):
    sum = 0
    for digit in range(1, n + 1):
        if n % digit == 0:
            sum += digit
    return sum == n + 1


def goldbach(n):
    result = []
    for digit in range(1, n):
        if is_prime(digit):
            a = digit
            b = n - a
            if is_prime(b) and (b, a) not in result:
                result.append((a, b))
    return result
