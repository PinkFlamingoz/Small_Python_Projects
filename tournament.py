# Import
import csv
import sys
import random
from basic_functions import get_valid_input


# Number of simulations to run
N = get_valid_input(int,"Enter the number of simulations to run: ")


# Main
def main():
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------
    if len(sys.argv) != 2:
    
        print("\nError 1: Too many or none arguments  \n Usage: python tournament.py [FILENAME.csv]\n")
        sys.exit(1)
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------

    #* Open files ---------------------------------------------------------------------------------------------------------------------------------------------
    teams = []
    with open(sys.argv[1], "r") as file:
         reader = csv.DictReader(file)
         for row in reader:
             teams.append({"team": row["team"], "rating": int(row["rating"])})
    #* Open files ---------------------------------------------------------------------------------------------------------------------------------------------
    
    # Simulate N tournaments and keep track of winning teams
    counts = {}
    for i in range(N):
        winner = simulate_tournament(teams)
        # If the winner is already in the dictionary, increment its value
        if winner in counts:
            counts[winner] += 1
        # If we encounter a new winning team, add it to the dictionary
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key = lambda team: counts[team], reverse = True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")
    # sorted(counts, key = lambda team: counts[team], reverse = True): 
    # The sorted function takes a list, tuple, or dictionary (in this case, counts) and returns a new, sorted list. 
    # The key argument specifies a function of one argument that is used to extract a comparison key from each element in the iterable. 
    # In this case, it's a lambda function that takes a team as input and returns the value of counts[team]. 
    # The reverse = True argument tells sorted to sort in descending order.
    # for team in sorted(...):: This is a for loop that will iterate over each item in the sorted list returned by the sorted function. 
    # On each iteration, the variable team will hold the current item.
    # print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning"): 
    # This line will be executed once for each team in the sorted list. 
    # The print function outputs a formatted string to the console. 
    # The string contains placeholders (like {team} and {counts[team] * 100 / N:.1f}), 
    # which will be replaced by the values of the respective expressions. 
    # In particular, {counts[team] * 100 / N:.1f} is an expression that calculates the percentage of games that the team has won, rounded to one decimal place.


# Simulate a game. Return True if team1 wins, False otherwise 
def simulate_game(team1, team2):
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability
# rating2 - rating1: This calculates the difference in ratings between the two players or teams. 
# If rating2 is greater than rating1, the result is positive, indicating that the second team is favored. 
# If rating1 is greater than rating2, the result is negative, indicating that the first team is favored.
# ((rating2 - rating1) / 600): This scales the difference in ratings. 
# In the Elo system, a difference of 200 points between two players' ratings is intended to correspond to a 75% expectation of winning for the higher-rated player. 
# The 600 in the denominator adjusts the scale so that the formula gives the expected probabilities that align with this intention.
# 10 ** ((rating2 - rating1) / 600): This raises 10 to the power of the scaled rating difference. 
# This step greatly magnifies the effect of rating differences. Even small differences in ratings can lead to large differences in expected outcomes.
# 1 + 10 ** ((rating2 - rating1) / 600): This adds 1 to the result from the previous step. This guarantees that the denominator in the final fraction is always greater than 1, which in turn ensures that the final probability is between 0 and 1.
# 1 / (1 + 10 ** ((rating2 - rating1) / 600)): This inverts the result from the previous step. The result is a probability that represents the expected outcome of the match for the first player or team. 
# If this probability is close to 1, the first team is expected to win; if it's close to 0, the second team is expected to win.

# Simulate a round. Return a list of winning teams
def simulate_round(teams):
    winners = []

    # Simulate games for all pairs of teams 
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


# Simulate a tournament. Return name of winning team 
def simulate_tournament(teams):
    # Simulate_round() returns a list of teams that have won the round. 
    # The list is then passed to simulate_round() again. 
    # This process continues until only one team is left. 
    # The team that has won the tournament is returned.
    while len(teams) > 1:
        teams = simulate_round(teams)
    return teams[0]["team"]


# Start
if __name__ == "__main__":
    main()
