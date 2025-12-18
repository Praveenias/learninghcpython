nums = [-1,-2,-3,-4,3,2,1]
product=nums[0]
for i in nums[1:]:
  product *= i
print(product)