def simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI

P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate (R): "))
T = float(input("Enter Time (T): "))

result = simple_interest(P, R, T)

print("Simple Interest:", result)