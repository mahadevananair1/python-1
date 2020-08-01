numbers = []
final_num = 10

def main():
    i = 0
    while i < final_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

main()
print("The numbers: ")

for num in numbers:
    print(num)
