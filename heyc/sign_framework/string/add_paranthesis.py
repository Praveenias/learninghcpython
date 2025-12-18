class Solution:
    def diffWaysToCompute(self, expression: str) :
      operations = {
         "+":lambda x,y:x+y,
         "-":lambda x,y:x-y,
         "*":lambda x,y:x*y
      }

      def backtrack(left,right):
        res = []
        for i in range(left,right+1):
          op = expression[i]
          if op in operations:
              nums1 = backtrack(left,i-1)
              nums2 = backtrack(i+1,right)
              print(nums1,nums2)

              for n1 in nums1:
                for n2 in nums2:
                  res.append(operations[op](n1,n2))
        if res == []:
           res.append(int(expression[left:right+1]))
        return res 

      return backtrack(0,len(expression)-1)
        
    def calculate(self, s: str) -> int:
      ans = 0
      num = 0
      sign = 1
      stack = [sign] 
      for c in s:
        if c.isdigit():
          num = num * 10 + int(c)
        elif c == '(':
          stack.append(sign)
        elif c == ')':
          stack.pop()
        elif c == '+' or c == '-':
          ans += sign * num
          sign = (1 if c == '+' else -1) * stack[-1]
          num = 0
        print(stack,num,ans)
      return ans + sign * num

    def maxRepeating(self, sequence: str, word: str) -> int:
      temp, res = word, 0
      while temp in sequence:
          print(temp)
          if temp in sequence:
              res += 1
              temp += word
      return res
if __name__ == '__main__':
  s = Solution()

  #print(s.diffWaysToCompute("2*3-1"))
  #print(s.calculate("1+1"))
  print(s.maxRepeating("ababbcab","ab"))
    