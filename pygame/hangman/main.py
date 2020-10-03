import random
import sys

secret_words = ["apple", "banana", "mango", "strawberry",
                "orange", "grape", "pineapple", "apricot",
                "lemon", "coconut", "watermelon", "cherry",
                "papaya", "berry", "peach", "lychee", "muskmelon"]
letter_guessed = ""
turn = 14

if __name__ == "__main__":
    random_fruit = random.choice(secret_words)
    print("Guess the word! HINT: word is a name of a fruit")

    for letter in random_fruit:
        print("_", end=" ")

    print("\n")

    while turn > 0:
        guess = input("Guess a letter: ")
        letter_guessed += guess
        failed = 0

        if guess == "":
            print("ENTER A LETTER")
        elif guess != "":
            for char in random_fruit:
                if char in letter_guessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
                    failed += 1

            if guess in random_fruit:
                print("\nCorrect")
            else:
                print("\nWrong")
                turn -= 1

            if failed == 0:
                sys.exit("You won")

        print(f"All guesses: {letter_guessed}")
        print(f"You have {turn} more chance to guess")
    print(f"The word was: {random_fruit}")
