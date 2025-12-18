s = 3600
h = s%24
s = s//24
m = s%60
s = s//60
print(f"{h}:{m}:{s}")