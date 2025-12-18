k = 3
arr = [12, -1, -7, 8, -15, 30, 16, 28]

result = []
queue = []
for i in range(k):
  if arr[i] < 0:
    queue.append(i)
i = k
for i in range(k,len(arr)+1):
  print(queue)
  if queue:
    result.append(arr[queue[0]])
  else:
    result.append(0)
  while queue and queue[0] < i-k+1:
    queue.remove(queue[0])
  if i < len(arr) and arr[i] < 0:
    queue.append(i)
  

print(result)
