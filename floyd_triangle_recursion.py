def printFloydTriangle(rows):   
    if(rows <= 0):
        return

    for i in range(1, printFloydTriangle.col+1):
        print(printFloydTriangle.num, end=" ")
        printFloydTriangle.num += 1
        
    print()
    printFloydTriangle.col += 1
    rows -= 1
    printFloydTriangle(rows) 

printFloydTriangle.col = 1
printFloydTriangle.num = 1
rows = int(input("Enter the Number of Rows: "))

print("Floyd's Triangle") 
printFloydTriangle(rows)