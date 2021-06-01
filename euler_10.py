def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_prime(limit):
    num = 2
    nums = []
    loop = True

    while loop:
        if check_prime(num):
            nums.append(num)

        if num >= limit:
            loop = False
            break

        if loop:
            if num == 2:
                num += 1
            else:
                num += 2
    nums.pop(-1)
    return sum(nums)

print(sum_prime(17))
