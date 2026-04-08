def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest:", si)


P = float(input("Enter P: "))
R = float(input("Enter R: "))
T = float(input("Enter T: "))

simple_interest(P, R, T)