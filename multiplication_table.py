num = int(input("Enter a number: "))                            # taking input of the number of which you want multiplication table

for i in range(1,11):                                           # using for loop to print the table
    print("{0:<4d} X {1:4d} = {2:4d}".format(num,i,num*i))      # printing the values using format() function

