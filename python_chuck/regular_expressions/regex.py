import re
line = 'From jan.poonthong@uct.ac.za Sat Jun 5 09:14:16 2010'
y = re.findall('^From .*@([^ ]*)', line)
print(y)
