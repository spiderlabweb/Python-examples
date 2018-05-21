# Taking a number from user
num = int(input("Enter a number: "))
# initializing variable rnum to 0. It is used to store the reverse of num
rnum = 0
# initializing temp variable to num
temp = num
# Reversing the num and storing in rnum variable using while loop
while temp > 0:
    rnum = rnum*10 + (temp%10)
    temp = temp//10

# printing the reverse of the number
print("The reverse of the number",num,"is",rnum)