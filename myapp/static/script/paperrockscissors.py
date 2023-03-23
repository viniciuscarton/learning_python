import random
choice = input("Pick 0 for Rock, 1 for Paper or 2 for Scissors: ")
choice = int(choice)
random_number = random.randint(0, 2)

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

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

if random_number == 0:
    print(rock)
elif random_number  == 1:
    print(paper)
elif random_number  == 2:
    print(scissors)

play = str(choice) + str(random_number)
play = play.replace('0', '3')
play = int(play)

wins = [32, 13, 21]
tie = [11, 22, 33]

if play in wins:
    print("You won!")
elif play in tie:
    print("That's a tie!")
else:
    print("You lost!")

