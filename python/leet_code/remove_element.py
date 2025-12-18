def removeElement(nums, val) -> int:
  len_array = len(nums)
  right_changes = 0
  i = 0
  while i < len(nums):
    if nums[i] == val:
      nums.pop(i)
      right_changes +=1
    else:
      i +=1
  return len_array - right_changes




nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums,val)