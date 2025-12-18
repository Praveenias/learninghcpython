def getSecondLargest(arr):
  maxv = max(arr)
  smax = -1
  for i in arr:
      if i < maxv and i > smax:
        smax = i
      print(smax,maxv,smax)
  return smax
print(getSecondLargest([10,5,10]))
print(getSecondLargest([12, 35, 1, 10, 34, 1]))