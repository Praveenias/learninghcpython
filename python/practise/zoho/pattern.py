num = 5

for i in range(1,num+1):
  for j in range(num-i):
    print(" ",end='')
  for k in range(i,i+i):
    print(k,end = '')
  for l in range(k,i,-1):
    print(l-1,end = '')
  print()
  #print(num,i)
  #print(" " * (num-i) + str(i))