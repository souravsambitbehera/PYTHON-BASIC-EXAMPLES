def evaluate_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def evaluate_lcm(x, y):
    lcm = (x*y)//evaluate_gcd(x, y)

    return lcm


num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))

print("The L.C.M. is", evaluate_lcm(num1, num2))
