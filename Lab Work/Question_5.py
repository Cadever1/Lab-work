# Multiplication Table Generator
def table(n):
    if n < 0:
        print("Negative number are not allowed")
    else:
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)


num = int(input("Enter a number: "))
table(num)