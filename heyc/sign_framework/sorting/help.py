class Solution:
  def searchRange(self, nums, target: int):
    l = 0
    r = len(nums)-1
    out = [-1,-1]
    while l <= r:
      mid = (l + r)//2
     # print(nums[mid])
      if nums[mid] == target:
        i = mid - 1
        j = mid +1
        out = [mid,mid]
        while i >=0 and nums[i] == target:
          out[0] = i
          i-=1
        while j < len(nums) and nums[j] == target:
          out[1] = j
          j +=1
        return out

      elif nums[mid] < target:
        l = mid +1
      else:
        r = mid-1
    return out
      #print(l,r)
     # break

  def findMin(self, nums) -> int:
    l = 0
    r = len(nums)-1
    while l <r:
      mid = (l+r)//2

      if nums[mid] > nums[r]:
        l = mid +1
      else:
        r = mid
    return nums[l]
      
  def findPeakElement(self, nums) -> int:
    l = 0
    r = len(nums)-1
    while l < r:
      mid = (l+r)//2
      if nums[mid] > nums[mid+1]:
        r = mid
      elif ( mid >-1 and nums[mid] > nums[mid-1] ) and (mid < len(nums) and nums[mid] > nums[mid+1]):
        return mid

      else:
        l = mid+1
      
    return l

  def solve(self,ar,n) -> bool:
    sora = sorted(ar)
    for i in range(1,n-1):
      j = i
      print(j)
      while j >0 and ar[j] > ar[j-1] and ar[j] > ar[j+1]:
        ar[j],ar[j+1] = ar[j+1],ar[j]
        j -=1
      print(ar)
    return sora == ar
    #print(ar)

  def arrange(self, n, balls):
    pri = {
      'S':1,
      'W':2,
      'G':3
    }
    i = 1
    while i < n:
      j = i
      print(pri[balls[j]], pri[balls[j-1]])
      i +=1
      while j > 0 and pri[balls[j]] < pri[balls[j-1]]:
        balls[j],balls[j-1] = balls[j-1],balls[j]
        j -=1
    print(balls)

  def MaximumPile(self, piles):

      l1 = sorted(piles,reverse=True)
      
      stoner = len(l1)//3  
      print(l1,stoner) 
      i = 1   
      sum = 0
      while i < stoner+1:
        sum += l1[i*2-1]
        i+=1
      return sum
      #return sum([ for i in range(0,stoner)])

  def print_array(self, n, arr):
    for i in range(0,n-1,2):
      arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

  def solve(self, n, x, y):
    dict1 = {}
    for i in range(len(x)):
      dict1[x[i]] = y[i]
    print(dict1)
    s_dic1 = sorted(dict1)
    for i in s_dic1:
      print(dict1[i])

    #print(sorted(dict1))
    #for i in sorted

  def sortSentence(self, s: str) -> str:
    words = s[::-1].split()
    words.sort()
    print(words)
    result = [ word[1:][::-1] for word in words ]
    return ' '.join(result)
  
  def minimumSum(self, num: int) -> int:
    nums = sorted(str(num))
    return int(nums[0]+nums[2])+int(nums[1]+nums[3])
  
  def maxProductDifference(self, nums) -> int:
    l = 0
    sl = 0
    s = float('inf')
    ss = float('inf')
    for i in nums:
      if i < s:
        ss = s
        s = i
        
      elif i < ss:
        ss = i

      if i > l:
        sl = l
        l=i
      elif i > sl:
        sl= i
    print(l,sl,s,ss)
    return (l*sl)-(s*ss)


  def maxProduct(self, nums) -> int:
    l = 0
    sl = 0
    for i in nums:
      if i > l :
        sl = l
        l = i
      elif i > sl:
        sl = i
    return (l-1)*(sl-1)


    

if __name__ == '__main__':
  s = Solution()
  # out = s.searchRange([1],1)
  #out = s.findMin([4,5,6,7,0,1,2])
  #out = s.findPeakElement([1,2,3,1])
  #out = s.solve([5 ,4, 3, 2, 1],5)
  #out = s.arrange(5,['S' ,'G' ,'W' ,'G' ,'S' ])
  #out = s.MaximumPile([43 ,68, 25])
  #out = s.print_array(5,[1 ,2 ,3 ,4 ,5])
  #out = s.solve(5,[8,3,9,2,4,5], [5,3,1,4,5,10])
  #out = s.sortSentence("is2 sentence4 This1 a3")
  #out = s.minimumSum(2932)
  #out = s.maxProductDifference([5,6,2,7,4])
  out = s.maxProduct([1,5,4,5])
  print(out)
