strs = ["dog","racecar","car"]

short = min(strs,key=len)
for item in strs:
    while len(short) > 0:
        if item.startswith(short):
            break
        else:
            short = short[:-1]
    print(short)
print(short)