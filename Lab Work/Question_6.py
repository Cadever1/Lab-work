#Salary Bonus Calcultor
def bonus(s, y):
    if y >= 10:
        b = s * 0.20
    elif y >= 5:
        b = s * 0.10
    else:
        b = s * 0.05
    print("Total Salary:", s + b)


n = int(input("Enter employees: "))

for i in range(n):
    s = float(input("Salary: "))
    y = int(input("Experience: "))
    bonus(s, y)