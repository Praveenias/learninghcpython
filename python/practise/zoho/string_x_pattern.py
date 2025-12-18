s = 'zohofinance'

for i in range(len(s)):
  for j in range(len(s)):
    if i == j or i+j == len(s)-1:
      print(s[i],end='')
    else:
      print(" ",end = '')
  print()