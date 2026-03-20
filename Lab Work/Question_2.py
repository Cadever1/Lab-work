# Number Classification System
def check_number(num):
    # Positive / Negative / Zero
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")
    
    # Even / Odd (nested if)
    if num != 0:
        if num % 2 == 0:
            print("It is Even")
        else:
            print("It is Odd")
    
    print()  # line gap


numbers = [5, -3, 0, 8, -2, 7]

for n in numbers:
    check_number(n)