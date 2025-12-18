def solve(s):
  def traverse(index,memo):
    if index == len(s):
      return 1
    if index in memo:
      return memo[index]
    ans =0
    if s[index]!=0:
      ans +=traverse(index+1,memo)
    if index+1 < len(s) and (s[index] == 1 or s[index] == 2 and s[index+1]  <= 6):
      ans +=traverse(index+2,memo)
    memo[index] = ans
    return memo[index] 
  return traverse(0,{})


print(solve([1,2]))