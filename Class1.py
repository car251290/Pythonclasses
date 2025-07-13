# Function to calculate the average of a list of numbers
def calculate_average():
    # Step 1: Ask the user to type numbers separated by spaces
    numbers = input("Enter numbers separated by spaces: ")
    
    # Step 2: Split the string into a list (e.g., "5 10" becomes ["5", "10"])
    number_list = numbers.split()
    
    # Step 3: Set up variables to keep track of the total and how many numbers
    total = 0
    count = 0

    # Step 4: Go through each number in the list
    for num in number_list:
        num = float(num)     # Turn the text into a number
        total += num         # Add the number to the total
        count += 1           # Add 1 to the count of numbers
    
    # Step 5: Check if there were no numbers entered
    if count == 0:
        print("No numbers entered.")
        return
    
    # Step 6: Calculate the average (total divided by how many numbers)
    average = total / count

    # Step 7: Print the average, rounded to 2 decimal places
    print("The average is:", round(average, 2))

# Step 8: Call the function to make it run
calculate_average()


#Problem 2: Separate Even and Odd Numbers
def separate_pair_inpair():
    # Step 1: Ask the user to type numbers separated by spaces
    numbers = input("Enter numbers separated by spaces: ")

    # Step 2: Split the text into a list (e.g., "4 7 10" becomes ["4", "7", "10"])
    number_list = numbers.split()

    # Step 3: Create two empty lists to store pair and inpair numbers
    pair_numbers = []
    inpair_numbers = []

    # Step 4: Go through each number in the list
    for num in number_list:
        num = int(num)  # Turn the text into a number
        if num % 2 == 0:
            pair_numbers.append(num)     # If the number is divisible by 2, it's a pair number
        else:
            inpair_numbers.append(num)   # If not, it's an inpair number

    # Step 5: Show the results
    print("Pair numbers:", pair_numbers)
    print("Inpair numbers:", inpair_numbers)

# Step 6: Call the function to make it run
separate_pair_inpair()




# while True:




