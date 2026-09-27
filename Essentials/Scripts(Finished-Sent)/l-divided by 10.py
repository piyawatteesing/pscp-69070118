"""Divide by 10 checker"""

num = int(input())
result = []
remain = 0

def divide_ten(num):
    """Divide by 10 checker"""
    if num % 10:
        remain = num % 10
        num = num - remain
        result.append(num)
        print("remain", remain) #for debugging
    elif num % 10 == 0:
        result.append(num)

    while num > 0:
        result.append(num - 10)
        num -= 10

if num < 0:
    pass
else:
    divide_ten(num)

print(*result)
