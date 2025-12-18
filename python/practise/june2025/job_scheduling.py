def jobSequencing(deadline, profit):
  n = len(deadline)
  temp = sorted(zip(profit,deadline),reverse=True)
  deadl = [-1]*n
  profit = job = 0
  for cp,cd in temp:
    start = min(n,cd-1)
    for i in range(start,-1,-1):
      if deadl[i] == -1:
        deadl[i] = 0
        profit += cp
        job +=1
        break
  return [job,profit]




print(jobSequencing([4, 1, 1, 1],[20, 10, 40, 30]))
print(jobSequencing([2, 1, 2, 1, 1],[100, 19, 27, 25, 15]))
print(jobSequencing([3, 1, 2, 2],[50, 10, 20, 30]))