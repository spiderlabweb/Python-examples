# taking first number
num1 = int(input("Enter first number: "))           
# taking second number
num2 = int(input("Enter second number: "))          
# taking third number
num3 = int(input("And Enter third number: "))  
 
if (num1 > num2) and (num1 > num3):
   max = num1
elif (num2 > num1) and (num2 > num3):
   max = num2
else:
   max = num3

# printing the max
print("The largest among these three numbers is",max)