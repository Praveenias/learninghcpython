class Solution:
    def shipWithinDays(self, weights, days) -> int:
        right = sum(weights)
        i= 0
        while i < right:
            mid = (i + right)//2
            print(mid,self.check_capacity(mid,weights,days))
            if self.check_capacity(mid,weights,days):
                right = mid
            else:
                i = mid +1

        return i
    def check_capacity(self,num,weights,days):
        sum = 0
        if num == 0:
            return False
        i= min(weights)
        j = len(weights)
        nume = 0
        while i < j:
            sum +=weights[i]
            if sum >= num:
                nume +=1
                sum = weights[i]
            if nume > days:
                return False
            i +=1
        return True
        

if __name__ == '__main__':
  s = Solution()
  print(s.shipWithinDays([1,2,3,1,1],4))