import random

secret_words = ["apple", "banana", "mango", "strawberry",
                "orange", "grape", "pineapple", "apricot",
                "lemon", "coconut", "watermelon", "cherry",
                "papaya", "berry", "peach", "lychee", "muskmelon"]


def split(word):
    return [char for char in word]


if __name__ == "__main__":
    random_fruit = random.choice(secret_words)
    split_random_fruit = split(random_fruit)

    print(split_random_fruit)
    print(random_fruit)

    for letter in random_fruit:
        print("_", end=" ")

    print("\n")

    guess = input("Guess a letter or a word: ")

    # TODO(jan) Fixed the user input with letters
    if guess == split_random_fruit:
        print("Correct")
    else:
        print("Wrong")
