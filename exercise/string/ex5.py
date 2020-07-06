def main(str1, str2):
    char1 = str1[:2] + str2[-1:]
    char2 = str2[:2] + str1[-1:]

    return char2 + ' ' + char1

print(main('abc', 'xyz'))
