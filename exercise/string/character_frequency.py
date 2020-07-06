def main():
    word = input('Enter a word: ')
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)

main()
