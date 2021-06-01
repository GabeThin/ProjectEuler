def smallest_mult(n):
    limit = n
    loop = True

    while loop:
        for i in range(1, limit + 1):
            if n % i != 0:
                break
            elif i == limit:
                num = n
                loop = False

        n += 1
    return num

print(smallest_mult(5))
