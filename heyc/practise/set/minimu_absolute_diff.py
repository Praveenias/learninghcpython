nums = [5 ,3, 2, 10 ,15]


def minAbsoluteDifference(nums, x):
  nums = sorted(nums)
  return abs(nums[0]-nums[x])
  # dict = {}
  # for i in range(len(nums)):
  #   dict[nums[i]] =i
  # for i in nums:
  #   diff = x + i
  #   if diff in nums:
  #     return abs(dict[diff] - dict[i])


print(minAbsoluteDifference([3 ,6 ,10, 14, 18],4)) #15
print(minAbsoluteDifference([1,2,3,4],3))
