nums=[8, 58, 71, 18, 31, 32, 63, 92, 43, 3 ,91, 93, 25, 80, 28]

con = sorted(nums)
res = []
for i in range(len(nums)):
  print(con[con.index(nums[i])+1])
#   print(con.index(nums[i])+1)
#   print(nums[con.index(nums[i])+1])
    # if nums[con.index(nums[i])+1] in nums[i:]:
    #     res.append(nums[con.index(nums[i])+1])
    # else:
    #     res.append(-1)
print(con)
