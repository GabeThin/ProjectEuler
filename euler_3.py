import math

def largest_prime_factor(num):
    x = 2

    while x <= num:
        if num % x:
            x += 1
        else:
            num = math.floor(num / x)

    return x

print(largest_prime_factor(13195))
