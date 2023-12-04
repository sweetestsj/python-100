import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
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

game_images = [rock, scissors, paper]
user_choice=int(input("make choice between rock=0,scissor=1,paper=2\n"))
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("draw")
elif (user_choice==0 and computer_choice==1) or (user_choice==1 and computer_choice == 2) or (user_choice==2 and computer_choice==0):
    print("you won")
else:
    print("you lost")