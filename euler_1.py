def multiples(limit):
    mult = 1
    nums = []



    while 5 * mult < limit or 3 * mult < limit:
        if 3 * mult not in nums:
            nums.append(3 * mult)
        if 5 * mult < limit and 5 * mult not in nums:
            nums.append(5 * mult)

        mult += 1

    return sum(nums)

while True:
    multiples(input())
    print()
