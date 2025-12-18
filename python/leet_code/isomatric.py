a = 'badc'
b = 'baba'

def isomatric():
  dict1 = {}
  dict2 = {}

  for i,j in zip(a,b):
    if((i in dict1 and dict1[i]!=j) or (j in dict2 and dict2[j] != i)):
      return False
    dict1[i] = j
    dict2[j] = i
  return True

print(isomatric())