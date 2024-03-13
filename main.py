# Initialize an empty list
my_list = []

# Get user input until they enter 'c'
while True:
  user_input = input("Enter an integer (or 'c' to compute the sum): ")

  # Check if user wants to quit
  if user_input.lower() == 'c':
    break

  # Convert input to integer and append to the list
  try:
    number = int(user_input)
    my_list.append(number)
  except ValueError:
    print("Invalid input. Please enter an integer.")

# Calculate the sum of the list
total_sum = sum(my_list)

# Print the result
print("The sum of the integers in the list is:", total_sum)
