def check_binary():
  nums = [1,3,5,6]
  expectec = 0
  left = 0
  right = len(nums)-1
  while left <= right:
    half = (left+right)//2
    if nums[half] == expectec:
      return half
    elif expectec < nums[half]:
      right = half-1
    else:
      left = half+1
  return half+1 if nums[half] < expectec else half
      
    
    
print(check_binary())
    