data = 'From jan.poonthong@uct.ac.za Sat Jun 5 09:14:16 2010'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)
