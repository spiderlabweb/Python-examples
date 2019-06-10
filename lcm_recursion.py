def lcm(x, y):
    lcm.multiple += y

    if((lcm.multiple % x == 0) and (lcm.multiple % y == 0)):
        return lcm.multiple
    else:
        return lcm(x, y)

lcm.multiple = 0
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    lcm = lcm(num2, num1)
else:
    lcm = lcm(num1, num2)

print("The L.C.M. of", num1,"and", num2,"is", lcm)