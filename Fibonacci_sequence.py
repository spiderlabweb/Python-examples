n = int(input("Enter a number: "))      # enter the number of terms of fibonacci sequence to print

pre = 0                                 # stores the previous value
cur=1                                   # stores the current value
for i in range(1,n+1):                  # loop to print n terms of fibonacci sequence
    print(cur,end=" ")                  # prints the current value
    temp=cur                            # stores the current value to temp variable
    cur = cur + pre                     # changes the current value by adding the prvious value to itself
    pre = temp                          # changes the previous value to temp value