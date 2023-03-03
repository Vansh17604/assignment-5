# assignment-5
# Get input from the user
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period in years: "))
rate = float(input("Enter the rate of interest: "))

# Calculate the simple interest
simple_interest = (principal * time * rate) / 100

# Print the result
print("The Simple Interest is:", simple_interest)
