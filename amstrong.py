num = 1634
order = len(str(num))
sum = 0
temp = int(num)
while temp > 0:
    digit = temp % 10
    sum += digit**order
    temp //= 10

if num == sum:
    print(f"The number {num} is an Amstrong number")
else:
    print(f"The number {num} is not an Amstrong number")
