data = 'From jan.poonthong@uct.ac.za Sat Jun 5 09:14:16 2010'
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
