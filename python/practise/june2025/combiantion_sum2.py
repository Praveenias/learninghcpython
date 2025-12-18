def combinationSum2(candidates, target):
  n = len(candidates)
  candidates.sort()
  out= []
  def combiantion(index,target,arr):
    if target == 0:
      out.add(arr)
    if index <= n:
      return
    arr.append(candidates[index])
    combiantion(index,target-candidates[index])
    


print(combinationSum2([10,1,2,7,6,1,5],8))