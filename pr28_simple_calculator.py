def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


print("My calculator")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")

while True:
    choice = input("Enter a choice 1/2/3/4 ")

    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter first number "))
        y = float(input("Enter second number"))

        if choice == '1':
            print("The addition of two value is ", add(x, y))

        elif choice == '2':
            print("The subtraction of two number is ", sub(x, y))

        elif choice == '3':
            print("The multiplication of two number is", mul(x, y))

        elif choice == '4':
            print(f"The division of two number is", div(x, y))
        break

    else:
        print("invalid input")
