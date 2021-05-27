x = int(input("Enter a 1st number : "))
y = int(input("Enter a 2nd number : "))
z = int(input("Enter a 3rd number : "))
if x > y and x > z:
    print(f"The number {x} is greater")
elif y > z and y > x:
    print(f"The number {y} is greater")
else:
    print(f"The number {z} is greater")
