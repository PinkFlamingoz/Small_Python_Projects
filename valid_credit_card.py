# Import
from basic_functions import get_valid_input


# Get credit card number from user
def get_credit_input():
    while True:
        card = get_valid_input(int ,"Enter credit card number: ")
        if card > 0:
            return card


# Get first two digits of credit card number
def get_first_digits(card):
    card_str = str(card)
    if len(card_str) > 1:
        two_digits = int(card_str[:2])
    else:
        two_digits = int(card_str[0])
    
    return two_digits


# Print card type
def print_card(card):
    check = calculate_checksum(card)
    card_str = str(card)
    length = len(card_str)
    first_digit = int(card_str[0])
    first_two_digits = int(card_str[:2])
    
    if check == 0:
        if length == 15 and first_two_digits in [34, 37]:
            print("Card is: AMEX")
        elif length == 16 and first_two_digits in [51, 52, 53, 54, 55]:
            print("Card is: MASTERCARD")
        elif first_digit == 4 and length in [13, 16]:
            print("Card is: VISA")
        else:
            print("Card is: INVALID")
    else:
        print("Card is: INVALID")


# Calculate checksum
# The divmod function in Python is a built-in function that takes two (non-complex) numbers as arguments, and returns a tuple containing the quotient and the remainder when the first number is divided by the second.
# The function is used as divmod(a, b), and its output is equivalent to (a // b, a % b). 
# Here, a // b is the integer division (or floor division) that returns the largest whole number not greater than the exact division result, and a % b is the modulo operation that returns the remainder of the division.
# print(divmod(17, 5))  # Output: (3, 2)
# In this case, dividing 17 by 5 gives a quotient of 3 and a remainder of 2, so the function returns the tuple (3, 2).
def calculate_checksum(card):
    card = str(card)
    digits = [int(x) for x in card[::-2]] + [sum(divmod(2 * int(x), 10)) for x in card[-2::-2]]
    return sum(digits) % 10
# card = str(card): This line converts the input number into a string. 
# The reason for this conversion is to make it easier to access individual digits in the card number. 
# In Python, strings are sequence types, which means that you can access elements in a sequence by their indices.
# digits = [int(x) for x in card[::-2]] + [sum(divmod(2 * int(x), 10)) for x in card[-2::-2]]: 
# This is a list comprehension, a compact way of creating a new list by iterating over an existing sequence and applying an expression to each element in the sequence. 
# This line consists of two list comprehensions that are concatenated with the + operator: 
# [int(x) for x in card[::-2]]: This part generates a list of every other digit in the card number, starting from the last digit. 
# The [::-2] slice means "start from the end, and take every second element". The int(x) converts each digit (which is a string) back into an integer.
# [sum(divmod(2 * int(x), 10)) for x in card[-2::-2]]: This part also generates a list of every other digit in the card number, but starting from the second-to-last digit. 
# For each of these digits, it first multiplies the digit by 2, then uses the divmod function to get the quotient and the remainder when this product is divided by 10. 
# It then takes the sum of the quotient and the remainder. This is equivalent to adding the digits of the number if it's a two-digit number, or simply keeping the number if it's a single digit. 
# return sum(digits) % 10: This line adds up all the digits in the digits list, and then takes the result modulo 10. 
# This will return 0 if the credit card number is valid according to the Luhn algorithm, or a non-zero number if it is not.


# Main
def main():
    card = get_credit_input()
    print_card(card)


# Start
if __name__ == "__main__":
    main()


# In Python, [:] is used for slicing sequences (like lists or strings). The general form is [start:stop:step]. This means "generate a new list (or string, etc.) by selecting every step-th element from start to stop".
# Here is what each argument does:
# 
# start: Specifies where the slice should start. If it's omitted, the slice starts from the beginning of the original sequence.
# 
# stop: Specifies where the slice should end. If it's omitted, the slice continues to the end of the original sequence.
# 
# step: Specifies the step size. If it's omitted, the slice includes every element from start to stop.
# 
# For example:
# [::2] will start at the beginning, go to the end, and take every second element. It gets every other element of the sequence.
# 
# [1::2] will start at index 1 (the second element), go to the end, and take every second element. It gets every other element, starting from the second one.
# 
# [::-1] will start at the end, go to the beginning, and take every element. It reverses the sequence.
# 
# [::-2] will start at the end, go to the beginning, and take every second element. It gets every other element of the sequence, but in reverse order.
#
# s = '123456789'
# print(s[::2])   # '13579'
# print(s[1::2])  # '2468'
# print(s[::-1])  # '987654321'
# print(s[::-2])  # '97531'