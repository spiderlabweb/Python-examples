# Recursive function for fibonacci sequence
def fib(n):
    if n <=1:
        # Base Case
        return n
    else:
        # Iterative case
        return fib(n-1) + fib(n-2)


# enter the number of terms of fibonacci sequence to print
n = int(input("Enter a number: "))     

# calling recursive fib function
for i in range(n):
    print(fib(i),end=" ")

