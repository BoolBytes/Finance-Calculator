import math

# Investment Calculator Functions
def get_investment_input():
    principal = int(input("How much money do you wish to deposit: "))
    interest_rate = int(input("What percentage is your interest rate (without including the '%' sign): "))
    interest_rate /= 100
    term = int(input("How many years do you plan on investing for: "))
    interest_type = input("Do you want 'simple' or 'compound' interest: ").lower()
    return principal, interest_rate, term, interest_type

def calculate_simple_interest(principal, interest_rate, term):
    return principal * (1 + interest_rate * term)

def calculate_compound_interest(principal, interest_rate, term):
    return principal * math.pow((1 + interest_rate), term)

def investment_calculator():
    principal, interest_rate, term, interest_type = get_investment_input()
    
    if interest_type == "simple":
        result = calculate_simple_interest(principal, interest_rate, term)
        print(f"Your total funds with simple interest is: {round(result)}")
    elif interest_type == "compound":
        result = calculate_compound_interest(principal, interest_rate, term)
        print(f"Your total funds with compound interest is: {round(result)}")

# Home Loan Repayment Calculator Functions
def get_bond_input():
    house_value = int(input("What is the current value of the house: "))
    interest_rate = int(input("What percentage is your interest rate (without including the '%' sign): "))
    interest_rate = (interest_rate / 100) / 12
    repay_months = int(input("How many months will it take you to repay the bond: "))
    return house_value, interest_rate, repay_months

def calculate_monthly_repayment(house_value, interest_rate, repay_months):
    return (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-repay_months))

def bond_calculator():
    house_value, interest_rate, repay_months = get_bond_input()
    result = calculate_monthly_repayment(house_value, interest_rate, repay_months)
    print(f"You will repay {round(result)} each month")

# Main Function
def main():
    print("Select the calculator:")
    print("1. Investment Calculator")
    print("2. Home Loan Repayment Calculator")

    choice = input("Enter the number of the calculator you want to use: ")

    if choice == "1":
        investment_calculator()
    elif choice == "2":
        bond_calculator()
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

# Entry Point
if __name__ == "__main__":
    main()