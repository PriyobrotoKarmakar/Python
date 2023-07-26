import random
word_list  = ["advark","baboon","contact"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

