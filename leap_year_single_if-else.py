# taking year in YYYY format
year = int(input("Enter the year: "))                           

# checking whether year is leap year or not
if year%400 == 0 or year%4 == 0 and year%100 != 0:
    print("{0} is a leap year.".format(year))
else: 
    print("{0} is not a leap year.".format(year))
