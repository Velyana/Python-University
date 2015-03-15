def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum += i
    if n == sum:
        return True
    else:
        return False

