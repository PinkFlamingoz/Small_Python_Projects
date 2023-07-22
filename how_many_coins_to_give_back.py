# Import
from basic_functions import get_valid_input


# Get the number of dollars the customer is owe
def get_dollars():
    while True:
            n = get_valid_input(float, "Change owed: ")
            if n >= 0:
                return n


# Calculate the number of quarters to give the customer
# The // operator divides and then rounds down to the nearest integer (e.g. 4.5 // 1 = 4)
def calculate_quarters(cents):
    quarters = cents // 25
    cents %= 25
    return quarters, cents


# Calculate the number of dimes to give the customer
def calculate_dimes(cents):
    dimes = cents // 10
    cents %= 10
    return dimes, cents


# Calculate the number of nickels to give the customer
def calculate_nickels(cents):
    nickels = cents // 5
    cents %= 5
    return nickels, cents


# Calculate the number of pennies to give the customer
def calculate_pennies(cents):
    pennies = cents // 1
    return pennies


# Main
def main():
    # Ask how many cents the customer is owed
    cents = round(get_dollars() * 100)
    coins = 0

    # Calculate the number of quarters to give the customer
    quarters, cents = calculate_quarters(cents)
    coins += quarters

    # Calculate the number of dimes to give the customer
    dimes, cents = calculate_dimes(cents)
    coins += dimes

    # Calculate the number of nickels to give the customer
    nickels, cents = calculate_nickels(cents)
    coins += nickels

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    coins += pennies

    # Print total number of coins to give the customer
    print(f"Total coins: {coins} Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies}")


# Start
if __name__ == "__main__":
    main()
