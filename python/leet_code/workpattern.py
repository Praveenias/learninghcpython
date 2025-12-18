
from itertools import zip_longest
pattern="abba"
s = "dog cat cat dog"
s_2l = s.split()
if(len(set(pattern)) == len(set(s_2l)) == len(list(set(zip_longest(pattern,s_2l))))):
    print("true")
else:
    print("false")
