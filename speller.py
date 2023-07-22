# Imports
import re
import sys
import time
from dictionary import check, load, size


# Maximum length for a word
# (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
LENGTH = 45

# Default dictionary
WORDS = "dictionaries/large.txt"

#* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Error 1: Too many or none arguments  \n Usage: python speller [DICTIONARY] [TEXT.txt] \n")
    sys.exit(1)
#* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------

# Benchmarks
time_load, time_check, time_size = 0.0, 0.0, 0.0

#* Open files ---------------------------------------------------------------------------------------------------------------------------------------------

# Determine dictionary to use
dictionary = sys.argv[1] if len(sys.argv) == 3 else WORDS

# Load dictionary
before = time.process_time()
loaded = load(dictionary)
after = time.process_time()

# Exit if dictionary not loaded
if not loaded:
    print(f"ERROR IN MAIN, Could not load {dictionary}.")
    sys.exit(2)

# Calculate time to load dictionary
time_load = after - before

# Try to open text
text = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]
file = open(text, "r", encoding="latin_1")
if not file:
    print("ERROR IN TEXT, Could not open {}.".format(text))
    sys.exit(3)
#* Open files ---------------------------------------------------------------------------------------------------------------------------------------------

# Prepare to report misspellings
print("\nMISSPELLED WORDS\n")

# Prepare to spell-check
word = ""
index, misspellings, words = 0, 0, 0

# Spell-check each word in file
while True:
    
    c = file.read(1)
    if not c:
        break

    if re.match(r"[A-Za-z]", c) or (c == "'" and index > 0): # Allow alphabetical characters and apostrophes
        word += c #------------------------------------------- Append character to word
        index += 1
        
        if index > LENGTH: #---------------------------------- Ignore alphabetical strings too long to be words
            
            while True: #------------------------------------- Consume remainder of alphabetical string
                c = file.read(1)
                if not c or not re.match(r"[A-Za-z]", c):
                    break
            
            index, word = 0, "" #----------------------------- Prepare for new word
    
    elif c.isdigit(): #--------------------------------------- Ignore words with numbers
        
        while True: #----------------------------------------- Consume remainder of alphanumeric string
            c = file.read(1)
            if not c or (not c.isalpha() and not c.isdigit()):
                break
        
        index, word = 0, "" #--------------------------------- Prepare for new word
   
    elif index > 0: #----------------------------------------- We must have found a whole word
        words += 1 #------------------------------------------ Update counter

        #----------------------------------------------------- Check word's spelling
        before = time.process_time()
        misspelled = not check(word)
        after = time.process_time()
        time_check += after - before #------------------------ Update benchmark

        #----------------------------------------------------- Print word if misspelled
        if misspelled:
            print(word)
            misspellings += 1

        index, word = 0, "" #--------------------------------- Prepare for next word

# Close file
file.close()

# Determine dictionary's size
before = time.process_time()
n = size()
after = time.process_time()

# Calculate time to determine dictionary's size
time_size = after - before

# Report benchmarks
print(f"\nWORDS MISSPELLED:     {misspellings}")
print(f"WORDS IN DICTIONARY:  {n}")
print(f"WORDS IN TEXT:        {words}")
print(f"TIME IN load:         {time_load:.2f}")
print(f"TIME IN check:        {time_check:.2f}")
print(f"TIME IN size:         {time_size:.2f}")
print(f"TOTAL TIME:           {time_load + time_check + time_size:.2f}\n")

# Success
sys.exit(0)