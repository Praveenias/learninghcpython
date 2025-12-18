nums = [-1]
k = 1

asum = 0
i = 0
maxave = nums[0]
for j in range(len(nums)):
  asum +=nums[j]
  
  if j-i+1 == k:
    print(i,j,j-i+1)
    temp = asum / (j-i+1)
    maxave = max(maxave,temp)
    
    asum -= nums[i]
    i +=1
print(maxave)

