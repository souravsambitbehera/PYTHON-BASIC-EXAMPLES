nterms = int(input("How many terms "))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("Enter a positive integer ")
elif nterms == 1:
    print("The fibonacci series of 0 is ", n1)
else:
    print("The fibonacci series of ", nterms)

    while count < nterms:
        print(n1, end=',')
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1

# print()
