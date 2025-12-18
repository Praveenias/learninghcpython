class Solution:
  def printReverse(self,n):
    if n == 0:
      return
    print(n)
    self.printReverse(n-1)
    print(n)
  
  def fact(self,n):
    if n <= 1:
      return 1
    return n * self.fact(n-1)
  
  def adddigit(self,n):
    if n <=9:
      return n
    return n%10 * self.adddigit(n//10)
  
  sum = 0
  def reverse(self,n):
    if n ==0:
      return
    self.sum = self.sum*10+(n%10)
    self.reverse(n//10)
    return self.sum
  
  def palindrome(self,n):
    return n == self.reverse(n)
    
  def countZeros(self,n,count):
    
    if n == 0:
      return count
    rem = n%10
    print(rem)
    if rem == 0:
      count +=1
    

    self.countZeros(n//10,count)
    return count
  
  def numberOfSteps(self, num: int) -> int:
    return self.help(num)

  def help(self,num,count=0):
      if num == 0:
          return count
      count +=1
      if num%2 == 0:
          
          return self.help(num/2,count)

      else:
          return self.help(num-1,count)
      
  def checkSorted(self,arr):
    if len(arr) == 1:
      return True
    
    return arr[0] < arr[1] and self.checkSorted(arr[1:])
  
  def linearSearchLast(self,arr,n,index=0):
    arr1 = []
    if index == -1:
      return arr1
    if arr[index] == n:
      arr1.append(index)
    return arr1 + self.linearSearchLast(arr,n,index-1)

    
  
if __name__ == '__main__':
  s = Solution()
  #out = s.printReverse(5)
  #out = s.fact(5)
  #out = s.adddigit(33)
  #out = s.reverse(3454)

  #out = s.palindrome(12321)
  #out = s.countZeros(100,0)
  #out = s.numberOfSteps(8)
  #out = s.checkSorted([1,2,4,10,13])
  out = s.linearSearchLast([1,4,3,4,4],4,4)
  print(out)