# taking input from user
num = int(input("Enter a number: "))        
# flag for if a number is prime or not
flag = True                                 

# the prime no. are greater than 1
if num > 1:                                 
    # going through every number btw 2 and num-1
    for i in range(2, num):                 
        # checking the num is divisible by no.
        if num % i == 0:                    
            # if does then flag = False, it's not a prime no.
            flag = False                     
            break
    if flag == False:
        # prints not a prime
        print("The number is not prime.")   
    else:
        # prints a prime
        print("The number is prime.")       
else:
    # prints not a prime
    print("The number is not prime.")       
