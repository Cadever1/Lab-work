def calculate_final_price():
    price = float(input("Enter price: "))
    discount = float(input("Enter discount percentage: "))
    
    final_price = price - (price * discount / 100)
    return final_price

result = calculate_final_price()
print("Final price after discount:", result)