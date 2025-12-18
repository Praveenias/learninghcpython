a = 'set'
b = 'step'

i = 0
j = 0

t = 0
a_len = len(a)
while j < len(b):
  if a[i] == b[j]:
    print(t)
    t +=1
    i+=1
  if i == a_len:
    print("yes")
  j +=1
