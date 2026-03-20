#ATM withdrawl style
def atm():
    balance = 10000

    while True:
        amt = float(input("Enter amount (0 to exit): "))

        if amt == 0:
            break
        elif amt < 0:
            print("Invalid amount")
        elif amt > balance:
            print("Insufficient balance")
        else:
            balance -= amt
            print("Withdrawn:", amt)
            print("Balance:", balance)

atm()