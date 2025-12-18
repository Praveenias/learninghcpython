def leftmin(arr):
  n = len(arr)
  leftminstack = []
  stack = [0]
  for i in range(len(arr)):
    while stack and stack[-1] >= arr[i]:
      stack.pop()
    if not stack:
      leftminstack.append(0)
    else:
      leftminstack.append(stack[-1])
    stack.append(arr[i])
  #print(leftminstack)

  stack = [0]
  right = []
  
  for i in range(n-1,-1,-1):
    while stack and stack[-1] >= arr[i]:
      stack.pop()
    if not stack:
      right.append(0)
    else:
      right.append(stack[-1])
    stack.append(arr[i])
  
  max = 0
  for i in range(n):
    if abs(right[n-i-1] -  leftminstack[i]) > max:
      max = abs(right[n-i-1] -  leftminstack[i])
  print(max,leftminstack,right)


leftmin([2 ,1,8])

#{0, 2, 4, 4, 4, 7, 2}