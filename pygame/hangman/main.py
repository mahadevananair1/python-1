import random

secret_words = ["apple", "banana", "mango", "strawberry",
                "orange", "grape", "pineapple", "apricot",
                "lemon", "coconut", "watermelon", "cherry",
                "papaya", "berry", "peach", "lychee", "muskmelon"]

letter_guessed = ""


def split(word):
    return [char for char in word]


if __name__ == "__main__":
    random_fruit = random.choice(secret_words)
    split_random_fruit = split(random_fruit)

    print("Guess the word! HINT: word is a name of a fruit")

    for letter in random_fruit:
        print("_", end=" ")

    print("\n")

    word_length = len(random_fruit)

    for time in range(word_length + 2):
        guess = input("Guess a letter: ")
        letter_guessed += guess

        for char in random_fruit:
            if char in letter_guessed:
                print(char)
            else:
                print("_")

        if guess in random_fruit:
            print("Correct")
        else:
            print("Wrong")

        print("Total:", letter_guessed)
