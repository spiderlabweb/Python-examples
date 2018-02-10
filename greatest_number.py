num1 = int(input("Enter first number: "))           # taking first number
num2 = int(input("Enter second number: "))          # taking second number
num3 = int(input("Enter third number: "))           # taking third number

max = num1                                          # assuming first number to max
if(num2 > max):                                     # checking if num2 is greater than max
    max = num2                                      # assigning num2 to max
elif(num3 > max):                                   # checking if num3 is greater than max
    max = num3                                      # assigning num3 to max
else:
    max = num1                                      # assigning num1 to max

print("The greatest number is ",max)                # printing the max