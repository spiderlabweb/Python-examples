# taking year in YYYY format
year = int(input("Enter the year: "))                           

# checking whether year is divisible by 4
if(year%4 == 0):                                                
    # checking whether year is divisible by 100
    if(year%100 == 0):                                          
        # checking whether year is divisible by 400
        if(year%400 == 0):                                      
            # printing the year is leap year
            print("The {0} is a leap year.".format(year))       
        else:
            # printing the year is not a leap year
            print("The {0} is not a leap year.".format(year))   
    else:
        # printing the year is leap year
        print("The {0} is a leap year.".format(year))           
else:
    # printing the year is not a leap year
    print("The {0} is not a leap year.".format(year))             
