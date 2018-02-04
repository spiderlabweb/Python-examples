num = int(input("Enter a number: "))        # taking input from user
flag = True                                 # flag for if a number is prime or not

if num > 1:                                 # the prime no. are greater than 1
    for i in range(2, num):                 # going through every number btw 2 and num-1
        if num % i == 0:                    # checking the num is divisible by no.
            flag = False                    # if does then flag = False, it's not a prime no. 
            break
    if flag == False:
        print("The number is not prime.")   # prints not a prime
    else:
        print("The number is prime.")       # prints a prime
else:
    print("The number is not prime.")       # prints not a prime
