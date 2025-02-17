import re
from mpmath import mp

mp.dps = 1000000
pi_string = str(mp.pi)

pattern = re.compile('121061')

result = pattern.search(pi_string)

if result:
    print(result.span())
else:
    print("No match")
