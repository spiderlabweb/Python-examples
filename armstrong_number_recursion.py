import math
# defining the getSum() recursive function
def getSum(num):
    if num == 0:
        # Base case
        return num
    else:
        # Iterative case
        return math.pow((num%10),3) + getSum(num//10)

# taking input and storing in num variable
num = int(input("Enter a number: "))
# initializing the sum variable by getting the sum from getSum()
sum = getSum(num)

# checking whether the sum is equal to num or not
if sum == int(num):
    # printing the num is an Armstrong number 
    print(num,"is an Armstrong Number.")    
else:
    # printing the num is not an Armstrong number
    print(num,"is not an Armstrong Number.")