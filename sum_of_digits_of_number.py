# taking number
num = int(input("Enter a number: "))

# initializing sum to zero
sum = 0
# going through every digit using every for loop
while num > 0:
    d = num%10
    num = num//10
    sum += d
    
    # we can write above code in single line
    # uncomment the below line and comment the above three lines
    # num,sum = num//10,sum+(num%10)

# printing the sum
print("The sum of digits of number is",sum)