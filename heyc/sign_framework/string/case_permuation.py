s = "a1b2"
res = []
for i in range(len(s)):
  if s[i].isalpha():
    res.append(s[:i]+s[i].upper()+s[i+1:])
    res.append(s[:i]+s[i].lower()+s[i+1:])
  print(res)


#orange
#