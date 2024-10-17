import random
game_items = ("r", "p", "s")

while True:
    choose = input("Rock, Paper, or Scissors? (r/p/s)\n")
    random_item = random.choice(game_items)  

    if choose in game_items:  
        if random_item == "r":
            print("Computer chose Rock")
        elif random_item == "p":
            print("Computer chose Paper")
        else:
            print("Computer chose Scissors")

        # Determine the result
        if choose == "r":
            if random_item == "s":
                print("Congratulations! You won")
            elif random_item == "p":
                print("You lost")
            else:
                print("Tie")
        elif choose == "p":
            if random_item == "r":
                print("Congratulations! You won")
            elif random_item == "s":
                print("You lost")
            else:
                print("Tie")
        elif choose == "s":
            if random_item == "p":
                print("Congratulations! You won")
            elif random_item == "r":
                print("You lost")
            else:
                print("Tie")
    else:
        print("Invalid item")

    choose_2 = input("Continue? (y/n)\n").lower()
    if choose_2 == "y":
        continue
    else:
        break