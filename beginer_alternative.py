# Procedures/functions for calculating the sum, difference, product, ratio, and square of two numbers.
def sum(num1, num2):
    return num1 + num2


def dif(num1, num2):
    return num1 - num2


def prod(num1, num2):
    return num1 * num2


def rat(num1, num2):
    return num1 / num2


def sqr(num1):
    return num1 ** num1

# Collecting numbers from user
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# displaying results of cumputation
print(f"The sum of {num1} and {num2} is {sum(num1, num2)}")
print(f"The difference between {num1} and {num2} is {dif(num1, num2)}")
print(f"The product of {num1} and {num2} is {prod(num1, num2)}")
print(f"The ratio of {num1} and {num2} is {rat(num1, num2):.2f}")
print(f"The square of {num1} is {sqr(num1)} and the square of {num2} is {sqr(num2)}")