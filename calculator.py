# defining add() function to add the numbers
def add(num1,num2):
    return num1 + num2

# defining sub() function to subtract the numbers
def sub(num1,num2):
    return num1 - num2

# defining mul() function to multiply the numbers
def mul(num1,num2):
    return num1 * num2

# defining div() function to divide the numbers
def div(num1,num2):
    return num1 / num2

print("CALCULATOR")
print("(1) Addition\n(2) Subtraction\n(3) Multiplication\n(4) Division")
choice = int(input("Which operation do you want to perform? "))
# taking and storing first number in num1 variable
num1 = int(input("Enter first number: "))   
# taking and storing second number in num2 variable
num2 = int(input("Enter second number: "))  

if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == 2:
   print(num1,"-",num2,"=", sub(num1,num2))
elif choice == 3:
   print(num1,"*",num2,"=", mul(num1,num2))
elif choice == 4:
    print(num1,"/",num2,"=", div(num1,num2))
else:
    print("Invalid Choice!")
