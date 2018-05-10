# taking an input
num = int(input("Enter a number: "))    

# checking whether a number is even using bitwise operator
if num&1:                          
    # if its odd then prints odd number
    print(num,"is an odd number.")    
else:
    # else prints even number
    print(num,"is an even number.")  