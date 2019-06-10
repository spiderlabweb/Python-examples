# taking input of the number of which you want multiplication table
num = int(input("Enter a number: "))                            

# using for loop to print the table
for i in range(1,11):                                           
    # printing the table using format() function
    print("{0:<3d} X {1:3d} = {2:<3d}".format(num,i,num*i))      

