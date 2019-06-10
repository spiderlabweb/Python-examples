# taking input and storing in num variable
num = int(input("Enter a number: "))

# finding order using len() and str() function
order = len(str(num))   
             
# initializing the sum variable by 0
sum = 0                      
# storing the num in temp variable                       
temp = num                  
   
# going through every digit of number store in temp variable                     
while temp > 0:                                     
    n = temp % 10
    temp = temp // 10
    # storing the sum of cube of the digits in sum variable
    sum = sum + pow(n,order)   
           
# checking whether the sum is equal to num or not               
if(sum == num):                 
    # printing the num is an Armstrong number                   
    print(num,"is an Armstrong Number.")          
else:
    # printing the num is not an Armstrong number
    print(num,"is not an Armstrong Number.")  