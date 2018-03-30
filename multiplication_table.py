# taking input of the number of which you want multiplication table
num = int(input("Enter a number: "))                            

# using for loop to print the table
for i in range(1,11):                                           
    # printing the values using format() function
    print("{0:<4d} X {1:4d} = {2:4d}".format(num,i,num*i))      

