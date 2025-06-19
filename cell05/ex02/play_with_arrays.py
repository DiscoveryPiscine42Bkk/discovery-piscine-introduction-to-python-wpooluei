# Define the original array of numbers
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new array by adding 2 to values greater than 5
new_array = [x + 2 for x in original_array if x > 5]

# Display both arrays
print("Original array:", original_array)
print("New array (only values > 5 + 2):", new_array)