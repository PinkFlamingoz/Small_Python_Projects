#imports
from basic_functions import get_valid_input


# Main
def main():
    # Menu
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    total = 0
    while True:
        item = get_valid_input(str, "\nChoose a meal (or type 'done' to finish): ")
        item = item.title().strip()
        if item == "Done":
            print("\nThanks for ordering!")
            break
        elif item in menu:
            total += menu[item]
            print(f"\nAdded {item} for ${menu[item]:.2f} Total is ${total:.2f}")
        
    print(f"\nYour total is ${total:.2f}")
        
        
# Start
if __name__ == "__main__":
    main()                  
