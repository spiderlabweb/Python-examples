start = int(input("Enter starting number of the interval : "))
end = int(input("Enter ending number of the interval : "))

print("Prime Numbers Between ", start, " and ", end, " : ")
for i in range(start, end+1):
    isPrime = True

    if(i <= 1):
        isPrime = False
    else:
        for j in range(2, int(i/2)):
            if(i % j == 0):
                isPrime = False
                break

    if (isPrime):
        print(i, end=" ")

print()
