def get_values():
    p = float(input("Enter P: "))
    r = float(input("Enter R: "))
    t = float(input("Enter T: "))
    return p, r, t


P, R, T = get_values()

SI = (P * R * T) / 100

print("Simple Interest:", SI)