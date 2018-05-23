# Taking a string from user
s = input("Enter a string: ")

# initializing variable rs to empty string(""). It is used to store the reverse of s
rs = ""

# checking for palindrome using the iterative method(for loop)
for i in s:
    rs = i + rs

# printing the reverse string
print("Reverse of string:",rs)