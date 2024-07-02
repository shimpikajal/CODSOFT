import random
def play_game():
  print("******************Here the Rock Paper sicssor game begin lets start************")
#first state the rules of this game 
print(" \n Rock vs paper : paper wins \n Rock vs scissor : Rock wins \n paper vs scissor : scissor wins.")
#first ask user to choose the one action / choice from giroven
user_choice = input("Enter a choice (rock, paper, scissors): ")

#now let computer choose the action / choice 
possible_choice = ["rock", "paper", "scissors"]
#use of random module 
computer_choice = random.choice(possible_choice)

print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

while True:
    play_game()
    answer = input("Do you want to play again? (yes/no): ").strip().lower()
    if answer != 'yes':
        print("Thanks for playing!")
        break
    
        
