# Taking a string from user
s = input("Enter a string: ")
# Reversing the string s and storing in rs variable using split
rs = s[len(s)::-1]
# Checking whether the given string and reversed string is same
if s == rs:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")