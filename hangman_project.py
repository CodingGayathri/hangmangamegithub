import random

# import hangman_stages

words = ["apple", "banana", "fried"]
lives = 6
choicen_word = random.choice(words)
world_length = len(choicen_word)
print(choicen_word)

# Initialize display with dashes
display = ["-" for _ in range(world_length)]
print(display)

game_over = False

while not game_over:
    guessed_letter = input("Enter a letter: ").lower()

    # Check if guessed letter is in the word and update the display
    for index in range(world_length):
        letter = choicen_word[index]
        if letter == guessed_letter:
            display[index] = guessed_letter

    print(display)

    # Reduce lives if the guessed letter is not in the word
    if guessed_letter not in choicen_word:
        lives -= 1
        print(f"Wrong guess. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lost!")

    # Check if the player has won
    if "-" not in display:
        game_over = True
        print("You won!!")
        