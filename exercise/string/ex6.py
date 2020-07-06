# Jan's code
def main(word):
    if len(word) == 3:
        return word + 'ing'
    elif len(word) < 3:
        return word
    elif 'ing' in word:
        return word + 'ly'
    else:
        return



print(main('ab'))
print(main('abc'))
print(main('string'))

# Good code
def add_string(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'

    return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
