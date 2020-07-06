def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Jan')
print(greet('es'), 'Devon')
print(greet('fr'), 'Strager')
