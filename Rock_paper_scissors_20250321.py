import random

print("Welcome to Rock, Paper, Scissors game \n You vs Computer")

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [Rock, Paper, Scissors]

user_choose = input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choose = int(user_choose)
if user_choose == 0: #or user_choose == "Rock" or user_choose == "rock" or user_choose == "ROCK":
  print("You chose Rock")

elif user_choose == 1: # or user_choose == "Paper" or user_choose == "paper" or user_choose == "PAPER":
    print("You chose Paper")

elif user_choose == 2: # or user_choose == "Scissors" or user_choose == "scissors" or user_choose == "SCISSORS":
    print("You chose Scissors")
else:
    print("Invalid input")
    exit()
print(images[user_choose])

computer_choose = random.randint(0, 2)
if computer_choose == 0:
    print("I choose Rock")
      
elif computer_choose == 1:
    print("I choose Paper")

else:
    print("I choose Scissors")
print(images[computer_choose])

if user_choose == computer_choose:
    print("It's a draw")
elif user_choose == 1 and computer_choose == 0 or user_choose == 2 and computer_choose == 1 or user_choose == 0 and computer_choose == 2:
    print("You win")
else:
    print("You lose")


