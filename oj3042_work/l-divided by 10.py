"""Divide by 10 checker"""

num = int(input())

for i in range(num, -1, -1):
    if i % 10 == 0:
        print(i, end=" ")
