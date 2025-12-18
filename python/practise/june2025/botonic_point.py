def findMaximum(arr):
  res = -1
  for i in range(len(arr)-1):
      if arr[i] > arr[i+1] and arr[i-1] < arr[i]:
          res = arr[i]
          return res
  return arr[-1]
print(findMaximum([10, 20, 30, 40, 50]))
print(findMaximum([120, 100, 80, 20, 0]))