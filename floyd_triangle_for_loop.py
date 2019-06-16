rows = int(input("Enter the Number of Rows: "))
num = 1

print("Floyd's Triangle") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print(num, end = ' ')
        num = num + 1
    print()