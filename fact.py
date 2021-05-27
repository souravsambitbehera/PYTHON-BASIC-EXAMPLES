num = int(input("Enter a number "))
fact = 1
if num < 0:
    print("The negative number of factorial does not exist")
elif num == 0:
    print("The factorial value is ", fact)
else:
    for i in range(1, num+1):
        fact = fact*i
    print(f"The {num} of factorial is {fact}")
