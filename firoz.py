import random
word_list= ["camel" ,"baboon","monkey","dog"]

chosen_word=random.choice(word_list)
print(chosen_word)

guess=input("Guess a letter: ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

