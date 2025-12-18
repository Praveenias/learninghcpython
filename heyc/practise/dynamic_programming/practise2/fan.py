def max_points(n, points):
  dp = [[-1 for j in range(4)] for i in range(n)]
  def traverse(row,last,dp):

    if dp[row][last] != -1:
      return dp[row][last]
    if row == 0:
      maxv = 0
      for i in range(3):
        if i !=last:
          maxv = max(maxv,points[0][i])
      dp[row][last] = maxv
      return maxv
    maxv = 0
    for i in range(3):
      if i != last:
        temp = points[row][i] +traverse(row-1,i,dp)
        maxv = max(maxv,temp)
    dp[row][last] = maxv
    return maxv
  out = traverse(n-1,3,dp)
  return out
print(max_points(4,[[1 ,2, 3],[3, 2 ,1],[1 ,2 ,3],[3 ,2 ,1]]))