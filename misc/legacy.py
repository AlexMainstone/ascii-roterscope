from string import ascii_uppercase
import math
import random

print("Hello,world!")

# Le factorial
def fact(x) -> int:
    return (x > 0) and fact(x-1) * x or 1


def explodingdie(d):
    roll = random.randrange(1, d+1)
    if roll == d:
        roll += explodingdie(d)
    return roll

print(explodingdie(2))

1

def reverseList(arr: list) -> list:
    n: int = len(arr)

    for i in range(0, math.floor(n / 2)):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

    return arr

print(reverseList(ascii_uppercase))
