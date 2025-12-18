nums = [5,0,1,2,3,4]

for i,j in enumerate(nums):
  # if nums[j] == i:
  #   continue
  nums[i],nums[j] = nums[j],nums[i]
  print(nums[i],nums[j])
  break

print(nums)
