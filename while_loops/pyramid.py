# Define the number of rows for the pyramid
rows = 5

# Initialize the outer loop counter
i = 1

# Outer loop: controls the number of rows
while i <= rows:
    # Print spaces before stars
    j = 1
    while j <= rows - i:
        print(" ", end="")  # print spaces
        j += 1
    
    # Print stars
    k = 1
    while k <= (2 * i - 1):
        print("*", end="")  # print stars
        k += 1
    
    # Move to the next line after each row
    print()
    
    # Increment row counter
    i += 1
