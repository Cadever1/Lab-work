# Palindrome Chaecker
def palindrome(x):
    s = str(x)
    rev = ""

    for i in s:
        rev = i + rev

    if s == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


val = input("Enter number or string: ")
palindrome(val)