# Example using the max() function
n = int(input("Enter the number of elements: "))
numbers = []

# Take n numbers as input
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find the maximum using max()
max_value = max(numbers)

print(f"The maximum value among the {n} numbers is: {max_value}")
