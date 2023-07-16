# If bank doses not say hello, it gives $100
def paycheck(words):
    # Define a dictionary to map greetings to their corresponding strings
    greeting_to_pay = {
        "hello": "$0",
        "how": "$20",
        "hey": "$20",
        "hi": "$20",
        "greetings": "$20",
        "howdy": "$20",
    }
    
    # Check if the list of words is empty
    if not words:
        return "$100"
    
    # Get the first word and convert it to lowercase
    first_word = words[0].lower().removesuffix(",")
    
    # Use the dictionary's get() method to return the corresponding string, 
    # or "$100" if the greeting is not in the dictionary
    return greeting_to_pay.get(first_word, "$100")

# Main
def main():
    text = input("Greeting: ")
    words = text.split()
    pay = paycheck(words)
    print(pay)


# Start
if __name__ == "__main__":
    main()
