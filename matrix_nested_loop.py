rows=int(input("Enter the Number Rows: "));
cols=int(input("Enter the Number Coloums: "));

# Initializing Matrix a with 0s
a = [[0 for j in range(0,cols)] for i in range(0,rows)]  
# Initializing Matrix b with 0s 
b = [[0 for j in range(0,cols)] for i in range(0,rows)]    
# Initializing Matrix sum with 0s
sum = [[0 for j in range(0,cols)] for i in range(0,rows)] 

print("Enter the Elements of Matrix a:")
for i in range(0,rows):
    for j in range(0,cols):
        print("Enter an Element (",i+1,",",j+1,"):", sep="", end=" ")
        a[i][j]= int(input())

print("Enter the Elements of Matrix b:")	
for i in range(0,rows):
    for j in range(0,cols):
        print("Enter an Element (",i+1,",",j+1,"):", sep="", end=" ")
        b[i][j]=int(input())

# Adding two Matrices
for i in range(0,rows):
    for j in range(0,cols):
        sum[i][j]=a[i][j]+b[i][j]

# Displaying the Matrix sum
print("Sum of Matrices is")
for i in sum:
    print(i)