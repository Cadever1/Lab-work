n = int(input("Enter N: "))

even_numbers = []

for i in range(2, n+1, 2):
    even_numbers.append(i)

print("Even numbers list:", even_numbers)