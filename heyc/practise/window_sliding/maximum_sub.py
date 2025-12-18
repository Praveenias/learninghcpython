nums = [-2,1,-3,4,-1,2,1,-5,4]
left = 0
maxv = 0

sumv =0
for j in range(len(nums)):
  #sumv +=nums[j]
  while left < j and sumv+nums[j] > sumv:
    sumv -= nums[left]
    left +=1
  sumv += nums[j]
  print(sumv)
  maxv = max(maxv,sumv)
print(maxv)
