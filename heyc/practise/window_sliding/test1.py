class Solution():
   def max_sum_subarray(self,arr,k):

    max_sum = sum(arr[:k])
    temp_sum = max_sum
    for i in range(0,len(arr)-k):
      temp_sum = temp_sum - arr[i] + arr[i+k] 
      max_sum = max(max_sum,temp_sum)
    return max_sum
  
   def min_subarray_length(self,arr, X):
    left = 0
    #right = len(arr)-1
    minv = float('inf')
    current_sum = 0
    for r in range(len(arr)):
      current_sum += arr[r]
      print(current_sum)
      while current_sum >X:
        minv = min(minv,r-left+1)
        current_sum -= arr[left]
        left +=1
    return minv if minv != float('inf') else 0
  
   def twoSum(self, numbers, target: int):
        i = 0
        j = len(numbers)-1
        while i < j:
            
            if numbers[j] + numbers[i]  ==  target:
                return [i+1,j+1]

            if numbers[j] + numbers[i]  >  target:
                j -=1
            else:
                i +=1

  # def removeDuplicates(self, nums) -> int:
  #    i = 0
  #    j = len(nums)-1
  #    while i < j:
  #       while i+1 < j and nums[i] == nums[i+1]:

   def maxLen(self, arr):
     zerocount = 0
     onecount = 0
     left = 0
     max_lenght = 0
     for r in range(len(arr)):
        if arr[r] == 0:
           zerocount +=1
        else:
           onecount +=1
        #print(zerocount,onecount)
        if zerocount == onecount:
           max_lenght = max(max_lenght,r-left+1)
     print(max_lenght)

   def smallestSubstring(self, S):
     has_map = {'0':0,'1':0,'2':0}
     left = 0
     min_hash = float('inf')
     for r in range(len(S)):
        has_map[S[r]] +=1
        while has_map['0'] > 0 and has_map['1'] >0 and has_map['2'] >0:
           min_hash = min(min_hash,r-left+1)
           has_map[S[left]] -=1
           left +=1
     return -1 if min_hash == float('inf') else min_hash
  
   def subarray_sum(self, arr, total_sum):
    left = 0
    c_sum = arr[0]
    for r in range(1,len(arr)):
      c_sum += arr[r]
      if left <= r and c_sum > total_sum:
          c_sum -= arr[left]
          left +=1
      if c_sum == total_sum:
         #print(arr[r],arr[left])
         return [left+1,r+1]
    return []
  
   def maxOfSubarrays(self, arr, k):
        arr1 = [max(arr[0:k])]
        left =1
        right = len(arr)-k+1
        #print(arr1)
        while left < right:
            arr1.append(max(arr[left+k-1], arr1[left-1]))
            #print(arr1)
            left +=1
        return arr1
  
   def longestKSubstr(self,s, k):
     hash_map = {}
     left = 0
     maxv = 0
     for r in range(len(s)):
        hash_map[s[r]] = hash_map.get(s[r],0) + 1
        while len(hash_map) > k and left < r:
           hash_map[s[left]] -= 1
           if hash_map[s[left]] == 0:
              del hash_map[s[left]]
           left +=1
        if len(hash_map) == k:
           maxv = max(maxv,r-left+1)
           
   def longestUniqueSubsttr(self,s):
     list1 = []
     left = 0
     maxv = -1
     for r in range(len(s)):
        while s[r] in list1:
          list1.remove(s[left])
          left +=1
        list1.append(s[r])
        maxv = max(maxv,r-left+1)
        print(list1,maxv)
     return maxv

   def maxLeno(self, arr):
      left = 0
      zeros = 0
      maxv = 0
      ones = 0
      out = []
      for r in range(len(arr)):
         if arr[r] == 0:
            zeros +=1
         else:
            ones +=1

         if zeros == ones:
            if maxv < r-left+1:
               maxv = r-left+1
               out = arr[left:r+1]
      return out

if __name__ == '__main__':
  s = Solution()
  #out = s.max_sum_subarray([0, 1, 10000] ,1)
  #out = s.min_subarray_length([0 ,1 ,10000],1)
  #out = s.maxLen([1,0,1,1,1,0,0])
  #out = s.twoSum([-1,0],-1)
  #out = s.smallestSubstring('12121')
  #out = s.subarray_sum([1, 4],0)
  #out = s.maxOfSubarrays([33 ,38 ,46 ,24 ,26 ,6 ,42 ,28],2)
  #out = s.longestKSubstr("aabacbebebe",3)
  #out = s.longestUniqueSubsttr("Heycoachsuper30")
  out = s.maxLeno([1, 0, 1, 1, 1, 0, 0])
  print(out)