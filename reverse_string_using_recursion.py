# defining the reverseString() recursive function
def reverseString(s):
    if len(s) == 1:
        return s
    else:
        return reverseString(s[1:]) + s[0]

# Taking a string from user
s = input("Enter a string: ")

# initializing variable rs to the return value from reverseString() function
rs = reverseString(s)

# printing the reverse string
print("Reverse of string:",rs)