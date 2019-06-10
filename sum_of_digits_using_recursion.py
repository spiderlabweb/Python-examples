# defining getDigitSum() function
def getDigitSum(num):
    if num == 0:
        return num
    else:
        return num%10 + getDigitSum(num//10)

# taking number
num = int(input("Enter a number: "))

# initializing sum to the return value of getDigitSum() function
sum = getDigitSum(num)

# printing the sum
print("The sum of digits of number is",sum)