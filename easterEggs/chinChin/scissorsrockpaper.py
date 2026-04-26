import random
game = random.randrange(0,3)
player = int(input("Scissor(0), Rock(1), Paper(2): "))

print(f"Computer played {game}")

if game == 0 and player == 0 or game == 1 and player == 1 or game == 2 and player == 2:
    print("Draw\n")

elif game == 0 and player == 1 or game == 1 and player == 2 or game == 2 and player == 0:
    print("You win\n")

elif game == 1 and player == 0 or game == 2 and player == 1 or game == 0 and player == 2:
    print("Computer wins\n")

else:
    print("invalid\n")
