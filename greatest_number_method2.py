# taking first number
num1 = int(input("Enter first number: "))           
# taking second number
num2 = int(input("Enter second number: "))          
# taking third number
num3 = int(input("And Enter third number: "))           

# assuming first number to max
max = num1                                          
# checking if num2 is greater than max
if(num2 > max):                                     
    # assigning num2 to max
    max = num2                                      
# checking if num3 is greater than max
elif(num3 > max):                                   
    # assigning num3 to max
    max = num3                                      
else:
    # assigning num1 to max
    max = num1                                      

# printing the max
print("The greatest among these three numbers is",max)                