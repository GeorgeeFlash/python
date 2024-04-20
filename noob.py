name = input("Enter your name: ")

for line in range(3):
    if line == 0:
        print("Roses are red")
    elif line == 1:
        print("Violets are blue")
    elif line == 2:
        print(f"And so is {name}")
    else:
        continue