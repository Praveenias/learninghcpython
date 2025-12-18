moves = "LLRRUD"
conf = {
  'U':'D',
  'D':'U',
  'L':'R',
  'R':'L'
}
list = []
num = 0
for i in moves:
  if i not in list:
    num +=1
    list.append(conf[i])
  if i in list:
    num -=1
    list.remove(i)
  # else:
  #   num -=1
  #   list.remove(conf[i])
print(num == 0,num)