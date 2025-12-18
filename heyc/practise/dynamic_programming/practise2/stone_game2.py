def stoneGameII(piles) -> int:
  dp = {}
  def traverse(A,I,M):
    if I == len(piles):
      return 0

    if (A,I,M) in dp:
      return dp[(A,I,M)]

    total = 0
    res = 0 if A else float('inf')
    for X in range(1,2*M+1):
      if I +X > len(piles):
        break
      total +=piles[I + X-1]
      if A:
        res = max(res,total + traverse(not A,I +X,max(M,X)))
      else:
        res = min(res,traverse(not A,I+X,max(M,X)))
    dp[(A,I,M)] = res
    return dp[(A,I,M)]
  return traverse(True,0,1)




print(stoneGameII([2,7,9,4,4]))