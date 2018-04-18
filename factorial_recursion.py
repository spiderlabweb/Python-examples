# defining the recursive function for finding factorial
def fac(n):
    if n <= 0:
        # Base case
        return 1
    else:
        # Iterative case
        return n * fac(n-1)

# Taking input from user
num = int(input("Enter a number:"))
#printing the factorial of the number by calling fac function
print("The factorial of the number is",fac(num))