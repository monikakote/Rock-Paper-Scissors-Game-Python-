import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors")
    
    # Get player's choice
    player_choice = input("Your choice: ").lower()
    
    # Validate input
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, please try again.")
        return
    
    # Get computer's choice
    computer_choice = get_computer_choice()
    print(f"Computer's choice: {computer_choice}")
    
    # Determine the winner
    result = get_winner(player_choice, computer_choice)
    print(result)

# Start the game
play_game()
