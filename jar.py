# Imports
from basic_functions import get_valid_input
import os


# Classes
class Jar:
    
    # Constructor
    def __init__(self, cookies = 0 ,capacity = 12):
        self._capacity = capacity
        self._size = cookies


    # Get cookies
    def __str__(self):
        return f'The jar currently has {self._size} cookies.'


    # Add cookies
    def deposit(self, n):
        try:
            if n + self._size > self._capacity:
                raise ValueError("Too many cookies.")
            self._size += n
            print(f"\n\t{n} cookies added.")
        except ValueError as e:
            print(f"\n\tError: {e}")


    # Take out cookies
    def withdraw(self, n):
        try:
            if n > self._size:
                raise ValueError("Too few cookies.")
            self._size -= n
            print(f"\n\t{n} cookies withdrawn.")
        except ValueError as e:
            print(f"\n\tError: {e}")


    # Get capacity
    @property
    def capacity(self):
        return self._capacity
    
    
    # Set capacity
    @capacity.setter
    def capacity(self, capacity):
        try:
            if capacity <= 0:
                raise ValueError("Capacity must be positive.")
            self._capacity = capacity
        except ValueError as e:
            print(f"\n\tError: {e}")


    # Get cookies
    @property
    def size(self):
        return self._size
    
    
# Main
def main():
    jar = Jar()
    while True:
        print_menu()
        case = get_valid_input(int, "\n\tEnter choice: ")
        if case == 1:
            jar.deposit((get_valid_input(int,"\n\tEnter number of cookies to deposit: ")))
        elif case == 2:
            jar.withdraw((get_valid_input(int,"\n\tEnter number of cookies to withdraw: ")))
        elif case == 3:
            print(jar)
        elif case == 4:
            capacity = jar.capacity
            print(f"{capacity} is the capacity of the jar")    
        elif case == 5:
            jar.capacity = get_valid_input(int,"\n\tEnter capacity of jar: ")
            print(f"\n\tCapacity of jar set to {jar.capacity}")
        elif case == 6:
            os.system("cls" if os.name == "nt" else "clear")
        elif case == 0:
            break
        else:
            print("\n\tInvalid choice.")
        input("\n\t\tPress Enter to continue...")


# Print the menu
def print_menu():
    options = [
        "Deposit cookies",
        "Withdraw cookies",
        "Get cookies",
        "Get capacity",
        "Set capacity",
        "Clear screen",
    ]

    print("\nWhat operation do you want to perform? Select Option number. Enter 0 to exit.\n")
    for i, option in enumerate(options, start = 1):
        print(f"\t{i}. {option}")
        

# Start
if __name__ == "__main__":    
    main()