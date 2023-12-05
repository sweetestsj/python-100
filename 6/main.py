import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
    display +="_"

print(f"game on, you have {len(stages)} lives")
print(display)

end_of_game=False
try_count = 0

while not end_of_game and try_count < len(stages):
    print(stages[try_count])
    guess = input(f"You have {len(stages)-try_count} lives, pick a letter\n").lower()
    for pos in range(len(chosen_word)):
        if guess==chosen_word[pos]:
            display[pos]=guess
    if guess not in chosen_word:
        print("Wrong guess, losing a life")
        try_count+=1
    print("End of round")
    print(' '.join(display))

    if "_" not in display:
        end_of_game = True

if end_of_game:
    print("you win")
else:
    print("you lost")

print(f"word was {chosen_word}")
