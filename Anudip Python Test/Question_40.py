def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

P = float(input("Enter P: "))
R = float(input("Enter R: "))
T = float(input("Enter T: "))

result = simple_interest(P, R, T)

print("Simple Interest:", result)