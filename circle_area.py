x = int(input("Enter a 1st number : "))
y = int(input("Enter a 2nd number : "))
z = int(input("Enter a 3rd number : "))
s = (x+y+z)/2
area = (s*(s-x)*(s-y)*(s-z))**.5
print(f"The area of circle is {area} ")
