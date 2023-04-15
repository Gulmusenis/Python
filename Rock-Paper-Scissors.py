import random

action_list = ["rock","paper","scissors"]

round_counter = 0
computer_score = 0
player_score = 0

total_rounds = input("How many rounds do you want to play? Please enter a number here:")

while True:
    round_counter += 1
    print("Round number:",round_counter)

    computer_choice = random.choice(action_list)
    player_choice = input("Please choose your action:")

    print(f"Computer:",{computer_choice},"\t","Player:",{player_choice})

    if computer_choice == player_choice:
        print("Tie! Both players chose the same action")
    
    elif computer_choice == 'paper':
        if player_choice == 'rock':
            print("Winner is:Computer")
            computer_score += 1
        else:
            print("Winner is:Player")
            player_score += 1

    elif computer_choice == 'scissors':
        if player_choice == 'paper':
            print("Winner is:Computer")
            computer_score += 1
        else:
            print("Winner is:Player")
            player_score += 1
  
    elif computer_choice == 'rock':
        if player_choice == 'scissors':
            print("Winner is:Computer")
            computer_score += 1
        else:
            print("Winner is:Player")
            player_score += 1
    
    if round_counter == int(total_rounds):
        break

if computer_score == player_choice:
    print("There is no winner, Tie",computer_score,":",player_score)
elif computer_score < player_score:
    print("Player won with score",computer_score,":",player_score)
elif computer_score > player_score:
    print("Computer won with score",computer_score,":",player_score)
