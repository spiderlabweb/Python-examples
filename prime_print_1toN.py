import math

end = int(input("Enter the end of the range : "))

print("Prime Numbers Between 1", " and ", end, " : ")

for i in range(2, end+1):
    isPrime = True

    for j in range(2, int(math.sqrt(i)+1)):
        if(i % j == 0):
            isPrime = False
            break

    if (isPrime):
        print(i, end=" ")

print()
