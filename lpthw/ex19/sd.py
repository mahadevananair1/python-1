def main(name, language, country, game):
    print(f"Your name is {name}")
    print(f"You code in {language}")
    print(f"You're in {country}")
    print(f"Favorite game is {game}")


def number(age, earn_money, spend):
    print(f"He is {age} year old")
    print(f"After five years, he will be {age + 5}")
    print(f"He earn {earn_money}")
    print(f"He spends {spend} per month\n")


print("Jan's:")
main('jan', 'python', 'thailand', 'arcade games')
number(16, 'zero', '1500')

print("Strager's:")
main('strager', 'c++', 'usa', 'arcade games')
number(28, '2000', '700')

print("Devon's:")
main('devon', 'java', 'canada', 'minecraft')
number(21, '1500', '500')
