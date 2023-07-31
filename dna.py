# Import
import csv
import sys


def main():
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------
    if len(sys.argv) != 3:

        print("\nError 1: Too many or none arguments  \n Usage: dna.py DATA/[databases.csv] sequences/[sequence.txt]\n")
        sys.exit(1)
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------

    # Read database file into a variable
    database = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Format the row dict so that it works for any number of rows
            row_data = {}
            for i in reader.fieldnames:
                row_data[i] = int(row[i]) if i != "name" else row[i]
            database.append(row_data)

    # Read DNA sequence file into a variable
    sequence = ""
    with open(sys.argv[2], "r") as file:
         sequence = file.read()

    # Find longest match of each STR in DNA sequence
    # Initialize an empty set
    # s_t_r = set()  
    # Loop through each item in database (each item is expected to be a dictionary)
    # for strs in database:
    #     # Then, loop through each key in the current dictionary
    #     for key in strs.keys():
    #         # If the key is not equal to 'name', add it to the set
    #         if key != 'name':
    #             s_t_r.add(key)
    # 
    # OR
    # 
    # Initialize an empty dictionary
    # s_t_r = {}
    # Loop through each dictionary in database
    # for strs in database:
    #     # Then, loop through each key in the current dictionary
    #     for key in strs.keys():
    #         # If the key is not equal to 'name'
    #         if key != 'name':
    #             # If the key is already in the dictionary, increment its value by 1
    #             if key in s_t_r:
    #                 s_t_r[key] += 1
    #             # Otherwise, add the key to the dictionary with a value of 1
    #             else:
    #                 s_t_r[key] = 1
    # 
    s_t_r  = {key for strs in database for key in strs.keys() if key != 'name'}
    
    # Initialize an empty dictionary
    # matches = {}  
    # Loop through each item in s_t_r
    # for i in s_t_r:
    #     # Get the result of longest_match for each item
    #     match = longest_match(sequence, i)  
    #     # Store each result in the dictionary under the corresponding key
    #     matches[i] = match  
    matches = {i: longest_match(sequence, i) for i in s_t_r}

    # Check database for matching profiles
    for i in database:
        # Remove the name so we can only check the strs
        i_copy = i.copy()
        i_copy.pop("name")

        if matches == i_copy:
            print(f"{i['name']}")
            return

    print("No match")

    return


# Returns length of longest run of subsequence in sequence
def longest_match(sequence, subsequence):
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


# Start
if __name__ == "__main__":
    main()    

