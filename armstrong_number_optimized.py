# taking input and storing in num variable
num = input("Enter a number: ")
# initializing the sum variable by 0
sum = 0

# going through every digit of number store in num variable   
for i in num:
    # storing the sum of cube of the digits in sum variable
    sum += pow(int(i),3)

# checking whether the sum is equal to num or not
if sum == int(num):
    # printing the num is an Armstrong number 
    print(num,"is an Armstrong Number.")    
else:
    # printing the num is not an Armstrong number
    print(num,"is not an Armstrong Number.")