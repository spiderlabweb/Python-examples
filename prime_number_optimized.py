import math
# taking input from user
num = int(input("Enter a number: "))         

# the prime no. are greater than 1
if num > 1:                                 
    # going through every number btw 2 and num-1
    # uncomment the below for loop to check it
    # for i in range(2,num//2):     
    # comment the below for loop to check above for loop
    for i in range(2,math.floor(math.sqrt(num))+1):          
        # checking the num is divisible by i.
        if num % i == 0:                    
            # prints num is not a prime number
            print(num,"is not a prime number.")                
            break   
    else:
        # prints num is a prime number
        print(num,"is a prime number.")       
else:
    # prints is not a prime number
    print(num,"is not prime number.")       