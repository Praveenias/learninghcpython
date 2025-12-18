def findMaxLength(nums):
  maxv = 0
  zerocount = 0
  onecount = 0
  for i in nums:
    if i == 0:
      zerocount +=1
    else:
      onecount +=1
    
    if zerocount == onecount and maxv  < (zerocount +onecount):
      maxv = zerocount + onecount
  return maxv

print(findMaxLength([0 ,1 ,1 ,0 ,1 ,1 ,0]))