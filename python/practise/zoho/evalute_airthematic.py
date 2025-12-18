s = "73421*+*-"

res = []
for i in range(len(s)):
  if s[i].isdigit():
    res.append(int(s[i]))

lenn = len(res)
# print(s[lenn])
k = len(s)
num = res[0]
for j in range(1,len(res)):
  print(s[lenn])
  if s[lenn] == '+':
    num += res[j]
  if s[lenn] == '-':
    num -= res[j]
  if s[lenn] == '*':
    num *= res[j]
  if s[lenn] == '/':
    num //= res[j]
  lenn +=1
print(num)

