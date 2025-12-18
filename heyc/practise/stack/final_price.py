list1 = [8,7,4,2,8,1,7,7,10,1]
res = []
stack = []
for i in range(len(list1)-1,-1,-1):
  if stack and stack[-1] > list1[i]:
    stack.pop()
  res.append(list1[i]- stack[-1] if stack else list1[i])
  stack.append(list1[i])
  print(stack)
print(res[::-1])
  

