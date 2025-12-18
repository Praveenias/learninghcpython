def dailyTemperatures(temperatures) :
  stack = []
  res = [0] * len(temperatures)
  for i in range(len(temperatures)):
    while stack and temperatures[i] > temperatures[stack[-1]]:
      idx = stack.pop()
      res[idx] = i-idx

    stack.append(i)
  print(res)
    
 # print(res)

dailyTemperatures([73,74,75,71,69,72,76,73])

    # while stack
