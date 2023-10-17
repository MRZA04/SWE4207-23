#This function checks whether or not the user wants to continue using the program
def check_continue():
    #Sets up while loop
    while True:
        #Asks the user to input if they want to continue and removes the white spaces in their input and makes it lower case
        user_input = input("Do you wish to continue (Y/N)? ").strip().lower()
        #A series of if, elif and else statements to that decide whether or not the while loop should continue or end
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

#Function to check if the user input is a valid integer
def check_numeric(prompt):
    #Sets up while loop
    while True:
        #Sets up user input to for all integer variables
        user_input = input(prompt)
        #If the user input is a digit, it will continue the program
        if user_input.isdigit():
            return int(user_input)
        #Else it will reset the while loop and asks the user to input a valid number.
        else:
            print("Invalid input. Please enter a numeric number.")

def computepay(hours, rate=10):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

while check_continue():
    hours = check_numeric("Enter the number of hours worked: ")
    rate = check_numeric("Enter the hourly rate (default is £10): ")
    pay = computepay(hours, rate)
    print(f"Total pay: £{pay:.2f}")