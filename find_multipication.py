num = int(input("enter a number "))
# using for loop

print(f"The multiplication table of {num} is : ")
'''
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
'''
# using while loop
i = 1
while i < 11:
    print(f"{num} X {i} = {num*i}")
    i += 1
