class Solution():
  def left_right_sum(self, nums):
    arr = []
    for i in range(len(nums)):
      n = sum(nums[:i]) + sum(nums[i+1:])
      arr.append(n)
    return arr
  
  def movetwos(self, nums):
    for i in range(len(nums)):
      if nums[i] == 2 :
        pass
    pass
  


if __name__ == '__main__':
  s = Solution()
  #out = s.left_right_sum([1 ,2 ,3 ,4 ,5])
  out = s.movetwos([2,2,1])
  print(out)
