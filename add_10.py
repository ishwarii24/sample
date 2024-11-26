# Initialize the sum to 0
total = 0

# Loop to take 10 numbers as input
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))  # Taking input
    total += num  # Adding the number to the total

print("The sum of the 10 numbers is:", total)
