import math

def pythag(n):
    loop = True
    b = 2

    while loop:
        for a in range(1, b):
            c = math.sqrt(a ** 2 + b ** 2)
            if str(c)[-1] == '0':
                c = int(c)
            if a + b + c == n and type(c) is int:
                loop = False
                break
        if loop:
            b += 1

    return a * b * c
print(pythag(1000))
