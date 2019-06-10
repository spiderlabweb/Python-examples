# defining the recursive function for finding factorial
def fac(num):
    if num <= 0:
        # Base case
        return 1
    else:
        # Iterative case
        return num * fac(num-1)

# Taking input from user
num = int(input("Enter a number:"))
#printing the factorial of the number by calling fac function
print("The factorial of the number is",fac(num))