import random

secret_words = ["apple", "banana", "mango", "strawberry",
                "orange", "grape", "pineapple", "apricot",
                "lemon", "coconut", "watermelon", "cherry",
                "papaya", "berry", "peach", "lychee", "muskmelon"]

random_fruit = random.choice(secret_words)
print(random_fruit)

for letter in random_fruit:
    print("_", end=" ")


# if __name__ == "__main__":
