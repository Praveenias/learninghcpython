import math

def kokoEat(arr,k):
  def caneat(val):
      hrs = 0
      for i in arr:
          hrs += math.ceil(i/val)
          # print(hrs,i,val,math.ceil(i/val),k)
      return hrs <= k
  arr = sorted(arr)
  l,r = 1,max(arr)
  res = r
  while l <= r:
      mid = (l+r)//2
      print("mid:",mid)
      if caneat(mid):
          res = mid
          r = mid-1
      else:
          l = mid+1
  return res


print(kokoEat([5 ,10 ,3],4))