# Menu Driven Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Divide-by-zero condition handle karna
    if b == 0:
        return "Error! Zero se divide nahi kar sakte."
    return a / b

def calculator():
    while True:
        print("\n--- Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Apni choice chunein (1-5): ")
        
        if choice == '5':
            print("Alvida! Calculator band ho raha hai.")
            break
            
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Pehla number dalein: "))
            num2 = float(input("Dusra number dalein: "))
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Kripya 1 se 5 ke beech chunein.")

# Calculator shuru karne ke liye
if __name__ == "__main__":
    calculator()