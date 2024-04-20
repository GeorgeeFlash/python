
# procedure for calculating the factorial of a number n
def fact(n):
    """fact(n): 
        This procedure calculates the factorial of 
        an input n from the user"""
    if n == 0:
        # base case 1
        return 1
    elif n == 1:
        # base case 2
        return 1
    elif n > 1:
        return n * fact(n - 1)


# Taking n from user and displaying it's factorial
try:
    count, n = 0, -1
    while n < 0:
        n = int(input("Enter n: "))
        if n < 0:
            print("No negative numbers :( dufes")
            count += 1
            if count == 3:
                print("You exausted your counts nigga!")
                exit()
except ValueError as e:
    print("What's wrong with you nigga! You got a ", e)
    print("Here's a hint: Only enter integers fool!")
    exit()
print(f"The factorial of {n} is {fact(n)}")
