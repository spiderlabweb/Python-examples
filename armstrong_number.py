num = int(input("Enter a number: "))                # taking input and storing in num variable
sum = 0                                             # initializing the sum variable by 0
temp = num                                          # storing the num in temp variable
while temp > 0:                                     # going through every digit of number store in temp variable
    n = temp % 10
    temp = temp // 10
    sum = sum + pow(n,3)                            # storing the sum of cube of the digits in sum variable
print("The sum is ",sum)                            # printing the sum
if(sum == num):                                     # checking whether the sum is equal to num or not
    print(num," is an Armstrong Number.")           # printing the num is an Armstrong number
else:
    print(num," is not an Armstrong Number.")       # printing the num is not an Armstrong number