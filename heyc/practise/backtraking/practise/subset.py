def subsets(nums):
 
  def traverse(index,arr):
    res.append(arr[:])
    for i in range(index,len(nums)):
      arr.append(nums[i])
      traverse(i+1,arr)
      arr.pop()
  res = []
  traverse(0,[])
  return res
  def backtrack(start,path):
    result.append(path[:])

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i+1,path)
        path.pop()
    
  result = []
  backtrack(0,[])
  return result



nums = [1,2,3]
out = subsets(nums)
print(out)