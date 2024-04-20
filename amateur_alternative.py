

def diamonds(n):
    mid = (n//2) + 1
    even = n % 2 == 0 # check if n is even or odd

    # For even numbers
    if even:
        space_constant = mid - 1
        for line in range(1, n + 1):
            if line < mid:
                space = space_constant - line
                print(space * ' ', end='')
                print('* ' * line)
            if line >= mid:
                mid -= 1
                space = space_constant - mid
                print(space * ' ', end='')
                print('* ' * mid)
    if not even:
        space_constant = mid
        for line in range(1, n + 1):
            if line <= mid:
                space = space_constant - line
                print(space * ' ', end='')
                print('* ' * line)
            if line > mid:
                mid -= 1
                space = space_constant - mid
                print(space * ' ', end='')
                print('* ' * mid)

try:
    n, count = 1, 1
    while n < 3:
        n = int(input("Enter the number of lines of your diamond (atleast 3): "))
        count += 1
        if count == 4:
            print("You exausted your counts!")
            exit()
    diamonds(n)
except ValueError as e:
    print(f'C\'mon nigga :(. You got a "{e}" error')

#    *       *          *
#   * *     * *        * *
#  * * *     *        * * *
#   * *               * * *
#    *                 * *
#                       *