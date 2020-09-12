nums = [1, 3, 4, 8, 9, 11, 12, 14, 15, 18, 20, 21, 23, 25, 29, 32, 34, 38, 41, 43, 45, 46, 49, 50]

value = int(input())

if value in nums:
    print("{} is in the list".format(value))
else:
    print("{} is not in the list".format(value))
