final_num = 10
jump = 2
element = []

def main():
    start_num = 0
    for i in range(start_num, final_num, jump):
        print(f"The current number is {i}")
        element.append(i)

        print(f"The number in the list {element}")
main()
print(f"The numbers: {element}")
