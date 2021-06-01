def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nth_prime(limit):
    num = 2
    repeats = 0
    loop = True

    while loop:
        if check_prime(num):
            repeats += 1

        if repeats == limit:
            break

        if num == 2:
            num += 1
        else:
            num += 2

    return num

print(nth_prime(10001))
