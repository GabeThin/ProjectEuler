import math

def palindrome(n):
    nums = []
    for x in range(10 ** (n - 1), (10 ** n)):
        for y in range(10 ** (n - 1), (10 ** n)):
            num = str(x * y)

            length = int(len(num) / 2) if len(num) % 2 == 0 else math.floor(len(num) / 2)

            half_1 = num[:length]
            half_2 = num[len(num)-1:length-1:-1]

            if half_1 == half_2:
                nums.append(num)
    return max(nums)

print(palindrome(3))
