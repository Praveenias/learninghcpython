def countWays(digits):
  n = len(digits)
  def traverse(digits,index):
    if index >=n:
      return 1
    ways = 0
    if digits[index]!=0:
      ways = traverse(digits,index+1)
    if (digits[index] =='1' and digits[index+1] <='2') or (digits[index] == '2' and digits[index+1] <= '6'):
      ways +=traverse(digits,index+2)
    return ways
  return traverse(digits,0)
    
print(countWays("123"))