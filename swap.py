num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping\nFirst Number: ",num1,"\nSecond Number: ",num2)

# swapping these two numbers without using temp variable

(num1,num2) = (num2,num1)

print("Swapped using temp variable")
print("After Swapping\nFirst Number: ",num1,"\nSecond Number: ",num2)