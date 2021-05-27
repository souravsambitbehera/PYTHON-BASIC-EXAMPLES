x = int(input("Enter a number"))
if x > 0:
    if x % 2 == 0:
        print(f"The number {x} is even")
    else:
        print(f"The number {x} is odd")
else:
    print("Enter a positive number")
