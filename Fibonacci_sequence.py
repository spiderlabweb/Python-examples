# enter the number of terms of fibonacci sequence to print
n = int(input("Enter a number: "))      

# stores the previous value
pre = 0                                 
# stores the current value
cur=1                                   
# loop to print n terms of fibonacci sequence
for i in range(1,n+1):                  
    # prints the current value
    print(cur,end=" ")                  
    # stores the current value to temp variable
    temp=cur                            
    # changes the current value by adding the prvious value to itself
    cur = cur + pre                     
    # changes the previous value to temp value
    pre = temp                          