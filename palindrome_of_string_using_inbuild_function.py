# Taking a string from user
s = input("Enter a string: ")
# Reversing the string s using in-build function
rs = ''.join(reversed(s))
# Checking whether the given string and reversed string is same
if s == rs:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")