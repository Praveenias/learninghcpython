class Solution:


  def selectionSort(self,nums):
    """ take ith element , find remaining list small element..swap it.
    """
    n = len(nums)
    for i in range(n):
      min_index = i
      for j in range(i+1,n):
        if nums[i] > nums[j]:
          min_index = j
      
      if min_index != i:
        nums[i],nums[min_index] = nums[min_index],nums[i]
      print(nums)
    return nums
  
  def bubblesort(self,nums):
    n = len(nums)
    count = 0
    for i in range(n):
      swapped = False
      for j in range(n-i-1):
        
        if nums[j] > nums[j+1]:
          nums[j+1],nums[j] = nums[j],nums[j+1]
          count +=1
          swapped = True
      print(nums)
     
      if not swapped:
        break
    print(count)

  def insertionsort(self,nums):
    for i in range(1,len(nums)):
      key = nums[i]
      j = i-1
      while j >=0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -=1
      nums[j+1] = key
    return nums

  def merge_sort(self,arr,left,right):
    
    if len(arr) > 1:
      mid = len(arr)//2
      leftl = arr[:mid]
      rightl = arr[mid:]
      self.merge_sort(leftl,0,mid)
      self.merge_sort(rightl,mid,len(arr))
      i = j = k = 0
      while i  < len(leftl) and j < len(rightl):
        if leftl[i] < rightl[j]:
          arr[k] = leftl[i]
          i+=1
        else:
          arr[k] = rightl[j]
          j +=1
        k +=1

      while i < len(leftl):
        arr[k] = leftl[i]
        i +=1
        k +=1

      while j < len(rightl):
        arr[k] = leftl[j]
        j +=1
        k +=1
    print(arr)

  def bubblesort(self,arr):
      count = 0
      for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
          if arr[j] > arr[j+1]:
            #print(arr[i],arr[j])
            arr[j],arr[i] = arr[i],arr[j]
           # print(arr[i],arr[j])
            count +=1
            swapped = True

        if not swapped:
          break
      return arr
  
  def game(self, a, b, n):
    print(self.bubblesort(a))
    print(self.bubblesort(b))

  def solve(self,inventory1, inventory2):
      #inventory1 = inventory1.split()
      #inventory2 = inventory2.split()
      arr = inventory1 +inventory2
      i = j = k = 0
      while i < len(inventory1) and j < len(inventory2):
        if inventory1[i] < inventory2[j]:
          arr[k] = inventory1[i]
          i +=1
        else:
          arr[k] = inventory2[j]
          j +=1
        k +=1
      while i < len(inventory1):
        arr[k] = inventory1[i]
        i +=1
        k +=1
      while j < len(inventory2):
        arr[k] = inventory2[j]
        j +=1
        k +=1
      return ' '.join(arr)

  def solve1(self, n, x, y):
    b= []
    for i in range(len(x)):
      b.append(y[i]-x[i])
    b = sorted(b)
    print(b)
    i = 0
    j = len(x)-1
    cnt = 0
    while i < j:
      if b[i]+b[j] >=0:
        cnt +=1
        i +=1
        j -=1
      else:
        i +=1
    return cnt

  def maximumSweetness(self, n, price, k):
      min = 0
      price = sorted(price)
      print(price)
  def getMedian(self, ar1, ar2, n, m):
      mid = (n+m )//2
      ar = sorted(ar1+ar2)
      print(ar)
      if (n+m) %2 == 0:
        #print(ar[mid])
        return (ar[mid]+ar[mid-1])//2
      return ar[mid]
  
  def findAndReplacePattern(self, words, pattern: str):
        l1 = []
        pattern_index = {}
        for i in range(len(pattern)):
            pattern_index[i] = pattern.index(pattern[i])

        for word in words:
            temp_dict = {i:word.index(word[i]) for i in range(len(word))}
            
            if pattern_index == temp_dict:
                print(word,temp_dict,pattern_index)
                l1.append(word)
        return l1

  def findTwoElement( self,arr):
      #l1 = []
      for i in range(1,len(arr)+1):
          if i not in arr:
              missing = i
              continue
          print(i)
          if arr.count(arr[i-1]) ==2 :
              repeat = arr[i-1]
      return [repeat,missing]
if __name__ == '__main__':
  s = Solution()
  #s.selectionSort([4,2,7,5,1])
  #s.bubblesort([1,2,3,7,5,1,0])
  #out = s.insertionsort([3,2,1])
  #s.merge_sort([5, 3, 1, 4, 5, 10],0,6)
  #s.game([7 ,2 ,8 ,9 ,5],[4, 6, 2, 5, 3],5)
  #print(s.solve(["book" ,"enchanted", "spell" ,"wand"],["ancient", "dragon", "magic", "scroll"]))
  #out = s.solve1(5, [8,3,9,2,4,5] , [5,3,1,4,5,10])
  #out = s.maximumSweetness(6,[13 ,5 ,1 ,8 ,21 ,2],3)
  #out = s.getMedian([1,5],[9,11],2,2)
  #out = s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb")
  out = s.findTwoElement([5, 1, 6, 2, 4, 6])
  print(out)

