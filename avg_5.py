# Initialize sum to 0
total = 0

# Loop to take 5 numbers as input
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))  # Taking input from user
    total += num  # Adding the number to the total

# Calculate the average
average = total / 5

print("The average of the 5 numbers is:", average)
