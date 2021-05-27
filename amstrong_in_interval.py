lower = 100
upper = 2000
for i in range(lower, upper+1):
    order = len(str(i))
    sum = 0

    temp = i
    while temp > 0:
        digit = temp % 10
        sum = sum+digit**order
        temp = temp//10

    if i == sum:
        print(i)
