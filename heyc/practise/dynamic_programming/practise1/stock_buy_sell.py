def maxProfit(prices) -> int:
  n = len(prices)
  def rec(prices,i,buyorsell,memo):
    if i == n:
      return 0

    if (i,buyorsell) in memo:
      return memo[(i,buyorsell)]
    if buyorsell:
      buy = rec(prices,i+1,False,memo) -prices[i] 
      skip = rec(prices,i+1,True,memo)
      maxprofit = max(buy,skip)
    else:
      sell = prices[i] + rec(prices,i+1,True,memo)
      skip = rec(prices,i+1,False,memo)
      maxprofit = max(sell,skip)
    memo[(i,buyorsell)] = maxprofit
    print(memo)
   
    return memo[(i,buyorsell)]
  return rec(prices,0,True,{})


print(maxProfit([7,1,5,3,6,4]))