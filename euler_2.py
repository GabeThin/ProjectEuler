def fibonacci_even(n):
    nums = []
    first = 1
    second = 2
    sum = 0

    nums.append(first)
    nums.append(second)

    while nums[-1] <= n:
        num = first + second

        nums.append(num)

        first = second
        second = num

    nums.pop(-1)

    for num in nums:
        sum += num if num % 2 == 0 else 0

    return sum

while True:
    print(fibonacci_even(int(input())))
    print()
