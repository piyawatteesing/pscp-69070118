"""what"""

num_a = int(input())
num_b = int(input())
div = int(input())
rem = int(input())

def dividation():
    for step in range(num_b - num_a):
        if (step % div) == rem:
            print(step + num_a)

dividation()