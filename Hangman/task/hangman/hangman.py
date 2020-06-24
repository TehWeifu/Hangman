# Write your code here
import random

print("H A N G M A N")

word_choice = random.choice(["python", "java", "kotlin", "javascript"])
unique_letters_choice = set(word_choice)
current_result = list("-" * len(word_choice))
input_set = set()
game_continue = True
lives = 8

menu = input('Type "play" to play the game, "exit" to quit: ')
while menu == "play":

    while game_continue:
        print("")
        print(''.join(current_result))
        guess = input("Input a letter: ")
        if len(guess) > 1:
            print("You should input a single letter")
        else:
            if guess.islower() == False:
                print("It is not an ASCII lowercase letter")
            else:
                if guess in input_set:
                    print("You already typed this letter")
                else:
                    input_set.add(guess)
                    if guess in unique_letters_choice:
                        for index in range(len(word_choice)):
                            if guess == word_choice[index]:
                                current_result[index] = guess
                        unique_letters_choice.discard(guess)
                    else:
                        if guess in word_choice:
                            print("No improvements")
                        else:
                            print("No such letter in the word")
                        lives -= 1

                    if lives < 1 or "-" not in current_result:
                        game_continue = False

    if "-" not in current_result:
        print("You survived!")
    else:
        print("You are hanged!")

    menu = input('Type "play" to play the game, "exit" to quit: ')


print("Thanks for playing!")
print("We'll see how well you did in the next stage")
