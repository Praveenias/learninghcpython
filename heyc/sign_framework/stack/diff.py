def find132pattern( nums):
      for i in range(1,len(nums)-1):
        print(nums[i])
        if nums[i-1] < nums[i] and nums[i] >nums[i+1]:
          return True
      return False

print(find132pattern([3 ,1 ,4 ,2]))