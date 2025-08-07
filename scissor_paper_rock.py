rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choice=["rock","paper","scissor"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
com_choice= random.randint(0,2)
print(choice[com_choice])
game_image=["rock","paper","scissors"]
if user_choice == com_choice:
    print("Draw")
elif user_choice==0 and com_choice==2:
    print("you lose")
elif user_choice==0 and com_choice==1:
    print("you win")
elif user_choice==1 and com_choice==0:
    print("you lose")
elif user_choice==1 and com_choice==2:
    print("you lose")
elif user_choice==2 and com_choice==0:
    print("you lose")
elif user_choice==2 and com_choice==1:
    print("you win")
else:
    print("enter valid number,you lost")
