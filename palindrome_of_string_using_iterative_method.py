# Taking a string from user
s = input("Enter a string: ")

# checking for palindrome using the iterative method(for loop)
for i in range(0,len(s)//2):
    if(s[i] != s[len(s)-i-1]):
        found = False
        break
else:
    found = True

# Checking whether the given string and reversed string is same
if found:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")