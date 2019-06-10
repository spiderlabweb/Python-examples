num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping\nFirst Number: ",num1,"\nSecond Number: ",num2)

# swapping these two numbers using temp variable

temp = num1
num1 = num2
num2 = temp

print("Swapped using temp variable")
print("After Swapping\nFirst Number: ",num1,"\nSecond Number: ",num2)
