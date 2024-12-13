import random
'''
1 for stone
-1 for paper
0 for scissors
'''

# Initialize scores
computer_score = 0
you_score = 0

# Dictionaries for choices and their string representations
youDict = {"s": 1, "p": -1, "sc": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissors"}

# Main game loop
while computer_score < 5 and you_score < 5:
    # Computer's random choice
    computer = random.choice([1, 0, -1])

    # User's input
    youstr = input("Enter your choice (s for Stone, p for Paper, sc for Scissors): ")
    if youstr not in youDict:
        print("Invalid input. Please enter 's', 'p', or 'sc'.")
        continue

    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    else:
        if (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
            print("You win this round!")
            you_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    # Display current scores
    print(f"Scores: You = {you_score}, Computer = {computer_score}\n")

# Determine the final winner
if you_score == 5:
    print("Congratulations! You won the game!")
elif computer_score == 5:
    print("Computer wins the game. Better luck next time!")
