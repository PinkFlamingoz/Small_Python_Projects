# Imports
import csv
from basic_functions import get_valid_input

# Get name and number
name = get_valid_input(str,"Name: ")
number = get_valid_input(str,"Number: ")

# Open CSV file
with open("DATA/phonebook.csv", "a") as file:

    # Print to file
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})
