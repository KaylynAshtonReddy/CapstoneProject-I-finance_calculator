# Request user input to select a finance option, convert to lower case
# use \n to add text onto new lines to space out the menu options

finance_type = input(
    "Choose either 'investment' or 'bond' from the menu below to proceed:\n"
    "investment     - to calculate the amount of interest you'll earn on interest \n"
    "bond           - to calculate the amount you'll have to pay on a home loan \n"
    "\n"
    "Enter in your selection: \n").lower()

# Conditions to force user to enter in the correct wording for the finance options
# Print an Error message if the spelling does
# not match the words'investment' or 'bond'
if finance_type == ("bond"):
    finance_type = ("bond")

elif finance_type == ("investment"):
    finance_type = ("investment")

# Removed error message

# Follow conditions if the user selected the 'investment' option
# Declare variables for the user input
if finance_type == ("investment"):
    deposit = (int(input("How much money are you deposting?: ")))

    interest_user_entered = (
        float(input("Enter in the interest rate (number only): ")))

    number_of_years = (
        int(input("Enter in the amount of years you plan on investing: ")))

    # Convert initially declared variables from user input to single letter variables
    P = deposit
    r = (interest_user_entered/100)
    t = number_of_years

    # Request additional input based on user input above
    interest = input(
        "What type of interest would you like: "
        " Simple or Compound ?\n"
        "Please enter in your selection: \n"
    ).lower()

    # Create additional nested condition for the interest type selction and calculate accordingly
    if interest == ("simple"):

        # 'A' as the total amount once the interest has been applied for simple interest
        # Simple interest calculation used and displayed
        # or compound interest will be calculated using the same variables
        # and be displayed
        A = P*(1+r*t)

        # Ammended the print statements as per guidance in review
        print("Your total amount once interest is earned is equal to R{}:".format(A))

    else:
        A = P * pow((1+r), t)

        # Ammended the print statements as per guidance in review
        print(
            "Your total amount once interest is earned is equal to R{:.2f}:".format(A))

# If user enters 'bond' the program will request additional input
# calculate the repayments and display the amount the user will pay
# each month
if finance_type == ("bond"):

    present_value = (
        int(input("What is the present value of the house?: ")))

    bond_interest_rate = (float(input("What is the interest rate "
                                      "that you are being charged?: ")))

    number_of_months = (float(input("What is the number of months that you plan"
                                    " to repay the bond: ")))

    # Variable names shortened
    # Divide interest rate by 1200 to convert it from annual to monthly interest
    # Divide number of months by 12 to get amount of years
    P = present_value
    i = bond_interest_rate / 1200
    n = number_of_months / 12

    # Formula to calculate the monthly repayments
    # Display the monthly repayment amount rounded to two decimals
    x = i * P / (1 - 1 / (1 + i) ** (n * 12))

    print("Your monthly repayments will be : R{:.2f}".format(x))
