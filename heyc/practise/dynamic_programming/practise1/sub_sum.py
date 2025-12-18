def sub(n,arr):
  def subsequence(index,sum,target):
    if index == n:
      if sum == target:
        return True
      return False
    sum += arr[index]
    subsequence(index+1,sum,target)
    sum -= arr[index]
    subsequence(index+1,sum,target)
  return subsequence(0,0,3)
print(sub(3,[1,2,3]))