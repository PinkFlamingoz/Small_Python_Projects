# Import
import re
from basic_functions import get_valid_input


# Get user text and return it
def get_user_text():
    return get_valid_input(str, "Enter Text:")


# Count the number of letters
def count_letters(text):
    # Use regular expressions to find all alphabetic characters and count them
    return len(re.findall('[a-zA-Z]', text))


# Count the number of words
def count_words(text):
    words = text.split()
    return len(words)


# Count the number of sentences
def count_sentences(text):
    # Use regular expressions to find all occurrences of '. ', '! ', '? ' and count them
    return len(re.findall('[.!?]', text))


# Calculate the grade by using the formula sing the formula:
# (0.0588 * L) - (0.296 * S) - 15.8
# Where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
def calculate_grade(letters, words, sentences):
    l = (letters / words) * 100
    s = (sentences / words) * 100
    return round((0.0588 * l) - (0.296 * s) - 15.8)


# Print the results
def print_results(letters, words, sentences, result):
    print(f"{letters} Letters!")
    print(f"{words} Words!")
    print(f"{sentences} Sentences!")
    print("Grade 16+" if result > 16 else "Before Grade 1" if result < 1 else f"Grade {result}")


# Main
def main():
    text = get_user_text()
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    grade = calculate_grade(letters, words, sentences)
    print_results(letters, words, sentences, grade)


# Start
if __name__ == "__main__":
    main()
