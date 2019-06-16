rows = int(input("Enter the Number of Rows: "))

num = 1
i = 1
print("Floyd's Triangle")
while(i <= rows):
    j = 1
    while(j <= i):        
        print(num, end = ' ')
        num = num + 1
        j = j + 1
    i = i + 1
    print()