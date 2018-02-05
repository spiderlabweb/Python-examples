num1 = int(input("Enter first number: "))               # taking first number
num2 = int(input("Enter second number: "))              # taking second number

facofnum1 = []                                          # list for factors of num1 variable
facofnum2 = []                                          # list for factors of num2 variable
commonfac = []                                          # list for common factors of both the numbers

for i in range(1,num1+1):                               # finding factors of num1
    if num1%i == 0: 
        facofnum1.append(i)

for i in range(1,num2+1):                               # finding factors of num2
    if num2%i == 0:
        facofnum2.append(i)

for fac in facofnum1:                                   # finging common factors of both the numbers
    if fac in facofnum2:
        commonfac.append(fac)

print("The GCD of the two numbers is ", commonfac[-1])  # printing right most number which is GCD of both numbers