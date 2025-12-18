s="rat"
t="cat"

if len(s) != len(t):
  print(False)

for i in s:
  if s.count(i) != t.count(i):
    print(False)

print(True)

