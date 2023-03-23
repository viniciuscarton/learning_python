import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, 2)]

# for i in chosen_word:
#     if guess in i:
#         print("Right")
#     else:
#         print("Wrong")

print(f'Pssst, the solution is {chosen_word}.')
display = []

word_length = len(chosen_word)
for i in range(word_length):
    display += "_"

lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end = False
while not end:
    guess = input("Guess a letter: ").lower()
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            end = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end = True
        print("You win.")
    print(stages[lives])


