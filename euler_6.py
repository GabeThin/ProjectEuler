def sum_square_difference(n):
    sum_square = 0
    sum = 0

    for i in range(n + 1):
        sum_square += i ** 2

    for i in range(n + 1):
        sum += i

    square_sum = sum ** 2

    return square_sum - sum_square

print(sum_square_difference(100))
