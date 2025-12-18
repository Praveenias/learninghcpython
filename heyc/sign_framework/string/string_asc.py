from collections import Counter
s = 'aaaabbbbcccc'

counter = Counter(s)
asc = True
res = ''

while counter:
  for i in sorted(counter) if asc else sorted(counter,reverse=True):
    res += i
    counter[i] -=1
    if counter[i] == 0:
      del counter[i]
    print(res)
  asc= not asc


print(res)