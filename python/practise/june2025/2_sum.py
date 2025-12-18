def minSum(arr):
  n = len(arr)
  temp1,temp2 = [],[]
  arr = sorted(arr)
  for i in range(0,n,2):
    temp1.append(str(arr[i]))
    if i+1 < n:
      temp2.append(str(arr[i+1]))
  temp1 = int(''.join(temp1))
  temp2 = int(''.join(temp2))
  return str(temp1+temp2)

print(minSum([6, 8, 4, 5, 2, 3]))
print(minSum([5, 3, 0, 7, 4]))