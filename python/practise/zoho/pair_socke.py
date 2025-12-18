num = [10,20,20,10,10,30,50,10,20]

hash_map = {}

cnt =0
for i in num:
  if i in hash_map:
    hash_map[i] +=1
    if hash_map[i] == 2:
      cnt +=1
      hash_map[i] = 0
  else:
    hash_map[i] = 1
  print(hash_map,cnt)
print(cnt)


