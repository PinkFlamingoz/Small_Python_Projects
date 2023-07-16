# Imports
import csv
import requests
from basic_functions import get_valid_input


# Main
def main():
    # Read NYTimes Covid Database
    download = requests.get("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)
    
    # Print out the new cases for each state
    for state, cases in new_cases.items():
        print(f"{state}: {cases}")
        
    # Create a list to store selected states
    states = []
    print("\nChoose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = get_valid_input(str, "State: ")
        state = state.title()
        if state in new_cases:
            states.append(state)
            
        # Exit the loop if user enters nothing    
        if len(state) == 0: 
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    # Dictionary to store new cases for each state
    new_cases = {}
    
    # Dictionary to store previous day's cases
    previous_cases = {}
    
    for row in reader:
        # Get the state and current day's cases
        state = row["state"]
        current_cases = int(row["cases"])

        # If this is the first time we've seen this state, initialize its data
        if state not in new_cases:
            new_cases[state] = []
            previous_cases[state] = current_cases
        else:
            # Calculate new cases by subtracting the previous day's cases
            new_case = current_cases - previous_cases[state]
            # Update previous cases with the current day's cases for the next iteration
            previous_cases[state] = current_cases
            # Add new cases to the list
            new_cases[state].append(new_case)

            # Keep only the most recent 14 days of new cases
            if len(new_cases[state]) > 14:  
                new_cases[state] = new_cases[state][-14:]
                # new_cases[state] = new_cases[state][-14:]: 
                # If the list of new cases for the current state has more than 14 elements, 
                # we're trimming it down to the most recent 14. 
                # The expression new_cases[state][-14:] gets the last 14 elements of the list.

    return new_cases


# Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        if state not in new_cases or len(new_cases[state]) < 14:
            print(f"Insufficient data for {state}")
            continue

        # Extract 7-day data for this week and last week
        last_week_cases = new_cases[state][:7]
        this_week_cases = new_cases[state][7:]

        # Calculate averages
        avg_last_week = sum(last_week_cases) / 7
        avg_this_week = sum(this_week_cases) / 7

        # Calculate percent change
        try:
            percent_change = ((avg_this_week - avg_last_week) / avg_last_week) * 100
            # Determine if it's an increase or decrease
            change = "increase" if percent_change > 0 else "decrease"
            # We just want the magnitude of the change
            percent_change = abs(percent_change)  
        except ZeroDivisionError:
            print(f"\n{state} had a 7-day average of {avg_this_week}, but percent change is undefined due to lack of previous data.")
            # Skip to the next state
            continue

        # Print output
        print(f"\n{state} had a 7-day average of {int(avg_this_week)} and an {change} of {percent_change:.1f}%.")


# Start
if __name__ == "__main__":
    main()                                                          