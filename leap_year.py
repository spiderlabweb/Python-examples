year = int(input("Enter the year: "))                           # taking year in YYYY format

if(year%4 == 0):                                                # checking whether year is divisible by 4
    if(year%100 == 0):                                          # checking whether year is divisible by 100
        if(year%400 == 0):                                      # checking whether year is divisible by 400
            print("The {0} is a leap year.".format(year))       # printing the year is leap year
        else:
            print("The {0} is not a leap year.".format(year))   # printing the year is not a leap year
    else:
        print("The {0} is a leap year.".format(year))           # printing the year is leap year
else:
    print("The {0} is not leap year.".format(year))             # printing the year is not a leap year
