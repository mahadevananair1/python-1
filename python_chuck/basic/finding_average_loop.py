count = 0
num = 0
print('Before', count, num)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    num = num + value
    print(count, num, value)
print('After', count, num, num / count)
