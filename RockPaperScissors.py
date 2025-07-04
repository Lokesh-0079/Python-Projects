import random 

options=("rock", "paper", "scissors")

is_running=True

while is_running:

    player = None
    com = random.choice(options)

    while player not in options:
        
        player=input("Enter your choice: ").strip().lower()
        
    print(f"player: {player}")
    print(f"computer: {com}")

    if player == com:
        print("It's a tie!")
    elif player == "rock" and com =="scissors":
        print("YOU WIN!")
    elif player == "scissors" and com =="paper":
        print("YOU WIN!")
    elif player == "paper" and com =="rock":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")


    while True:

        play_again=input("Do you wish to play again?(Y/N): ").strip().lower()
    
        if play_again  in ("y","n"):
            break
        print("Enter valid option!")
        if  play_again != "y":
            is_running = False

print("Thanks For Playing!")