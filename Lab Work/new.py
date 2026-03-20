#write a program to create a list of any 10 numbers and sort hem in decending order without use any libraby mwthod for sorrting
numbers = [12, 5, 8, 19, 3, 15, 7, 1, 10, 6]

# Sorting in descending order using Bubble Sort
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:  # Swap for descending order
            # Swapping
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# Print the sorted list
print("Sorted list in descending order:")
print(numbers)



























# The other method to solve this shit
nums = [12, 5, 8, 19, 3, 15, 7, 1, 10, 6]

n = len(nums)

for i in range(n):
    for j in range(n - 1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("Sorted list:", nums)