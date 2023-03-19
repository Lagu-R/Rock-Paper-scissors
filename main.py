import random
# Rock / Paper / scissors Game
# Rock  == 0
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
# Paper  == 1
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
# Scissors  == 2
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
# Game components list
game_box = [rock, paper, scissors]
# player Turn
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3:
  print("You Typed an invalid number, You Lose!")
print(game_box[choice])
# space between choice
print("_      _      _      _      _      _      _")
# computer turn 
print("\nComputer Choose:\n")
enemy = random.randint(1, 3)
enemy_step = enemy - 1
enemy_turn = game_box[enemy_step]
print(enemy_turn)
# RULES

  # Rock wins against scissors.
if choice == 0 and enemy_step == 2:
  print("You Win!")
  # scissors win againts paper.
elif choice == 2 and enemy_step == 1:
  print("You Win!")
  # paper wins against rock.
elif choice == 1 and enemy_step == 0:
  print("You Win!")
  # Draw
elif choice == enemy_step:
  print("Draw!")
  # Else You lose ! :) :*
else:
  print("You Lose! 3:)\nTry Again ;)!")
