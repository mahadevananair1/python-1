def greet(lang):
    if lang == 'th':
        print('Sawadee')
    elif lang == 'es':
        print('Halo')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

while True:
    user = input('Choose a language [th, es, fr, en]: ')
    greet(user)
