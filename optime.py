# OpenAI, ChatGPT, Crewe AI Assistant
from itertools import permutations

# Define the initial state of the cans
piles = [[8, 10, 7], [10, 7, 9], [7, 9, 8]]

# Calculate the score for a given sequence of throws
def calculate_score(throws, piles):
    score = 0
    # Create a copy of the piles to keep track of the cans
    temp_piles = [pile.copy() for pile in piles]
    for i, throw in enumerate(throws):
        pile_index, can_index = divmod(throw, 3)
        score += (i + 1) * temp_piles[pile_index].pop(0)
    return score

# Generate all possible sequences of throws
possible_throws = permutations(range(9), 3)

# Find a sequence of throws that results in a score of 50
solution = None
for throws in possible_throws:
    if calculate_score(throws, piles) == 50:
        solution = throws
        break

# Translate the solution into the actual cans to be hit
if solution:
    solution_translated = [(throw // 3, throw % 3) for throw in solution]
    print("\n")
    print("Sequence to hit to score 50:", solution_translated)
else:
    print("It's not possible to score exactly 50 with any sequence of throws.")

# Unpack to be more descriptive   
first = solution_translated[0]
second = solution_translated[1]
third = solution_translated[2]

verbal = [["Top Row, Left - 8", "Top Row, Middle - 10", "Top Row, Right - 7"],
          ["Middle Row, Left - 10", "Middle Row, Middle - 7", "Middle Row, Right - 9"],
          ["Bottom Row, Left - 7", "Botton Row, Middle - 9", "Bottom Row, Right - 8"]]
print("\n")
print(verbal[first[1]][first[0]], ", ", verbal[second[1]][second[0]], ", ", verbal[third[1]][third[0]])


