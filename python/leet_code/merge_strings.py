word1="ab"
work2="pq"

out = ''
lar_chr = ''
if len(word1) == len(work2):
  pass
elif len(word1) < len(work2):
  lar_chr = work2[len(word1):]
else:
  lar_chr = word1[len(work2):]

for char in (tuple(zip(word1,work2))):
  out +=char[0]+char[1]
  print(char)

out +=lar_chr
print(out)
    