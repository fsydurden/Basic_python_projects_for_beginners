import random

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


print("welcome to Rock Paper Scissors")
user_choice = int(input("Enter 1 for rock \n 2 for paper \n and 3 for scissors\n"))
computer_choice = random.randint(1, 3)
if user_choice == computer_choice:
    print("Its a draw!")
elif user_choice == 1 and computer_choice == 2:
    print(rock)
    print("---------------------------------------")
    print(scissors)
    print("user wins!")
elif user_choice == 1 and computer_choice == 3:
    print(rock)
    print("---------------------------------------")
    print(scissors)
    print("User wins")
elif user_choice == 2 and computer_choice == 1:
    print(paper)
    print("---------------------------------------")
    print(rock)
    print("User wins")
elif user_choice == 2 and computer_choice == 3:
    print(paper)
    print("---------------------------------------")
    print(scissors)
    print("Computer wins")
elif user_choice == 3 and computer_choice == 1:
    print(scissors)
    print("---------------------------------------")
    print(rock)
    print("Computer wins")
elif user_choice == 3 and computer_choice == 2:
    print(scissors)
    print("---------------------------------------")
    print(paper)
    print("User wins")
else:
    print("Invalid input, try something different u donkey")
