######################################################################
# Dupchu Wangmo
# Software Engeering 
# Student ID: 02230282
#########################################################################
# REFERENCES
# https://chat.openai.com/c/4ae2f26f-6274-4f97-b81a-6f5e59b7a385
################################
# SOLUTION
# Your Solution Score: 49903
# Input file no.2
########################################################################

# Read the input.txt file
def read_input(file_path):
    rounds = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            rounds = [(line.split()[0], line.split()[1]) for line in lines]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return rounds

# solution
def calculate_score(rounds):
    shapes = {'A': 1, 'B': 2, 'C': 3}
    outcomes = {'X': 0, 'Y': 3, 'Z': 6}
    total_score = 0
    for round in rounds:
        opponent_move, outcome = round
        total_score += shapes[opponent_move] + outcomes[outcome]
    print(f"The total score is: {total_score}")
                                                                                                            
file_path = 'input_2_cap1.txt'
rounds = read_input(file_path)
if rounds:
    calculate_score(rounds)
