def gcd(num1,num2):
    if num1%num2 == 0:
        # Base case
        return num2
    else:
        # Iterative case
        return gcd(num2,num1%num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = (num1*num2)//gcd(num1,num2)

print("The L.C.M. of", num1,"and", num2,"is", lcm)