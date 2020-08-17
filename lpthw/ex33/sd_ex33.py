final_num = 5
element = []


def main():
    i = 0
    while i < final_num:
        print(f"The current number is {i}")
        element.append(i)

        i = i + 2
        print(f"The number in the list is {element}")
    print(element)


main()
