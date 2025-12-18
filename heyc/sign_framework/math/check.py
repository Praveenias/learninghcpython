import collections
class Solution:
    def gcd(self,a,b):
        if a %b == 0:
            return b
        return self.gcd(b,a%b)

    def hasGroupsSizeX(self, deck) -> bool:
        
        if len(deck) <=1:
            return False
        counter = dict()
        for i in deck:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        
        if len(counter) == 1:
            return True
        print(counter)
        g = counter[deck[0]]
        
        for i in counter.values():
            g = self.gcd(g,i)
            
            if g ==1:
                print(gc,i)
                return False
        return True

    def simplifiedFractions(self, n: int):
        list1 = []
        dup = []
        for i in range(1,n):
            for j in range(i+1,n+1):
                if i/j <1 and i/j not in dup:
                    list1.append(f"{i}/{j}")
                    dup.append(i/j)
                print(i/j,i,j)
        print(list1)

    def interchangeableRectangles(self, rectangles) -> int:
        rat = {}
        for i,j in rectangles:
            res= i/j
            if res in rat:
                rat[res] += 1
            else:
                rat[res] = 1
        out = 0
        for i in rat.values():
            out +=(i*(i-1))//2
        return out

    def maxCoins(self, piles) -> int:
        piles.sort()
        print(piles)
        n = len(piles)
        ans, i = 0, n//3
        print(n,i)
        while i < n:
            #print(piles[i])
            ans += piles[i]
            i += 2
        return ans

    def minTimeToVisitAllPoints(self, points) -> int:
        sum = 0
        for i in range(len(points)-1):
            x1,y1 = points[i]
            x2,y2 = points[i+1]
            sum += max(abs(x2-x1),abs(y2-y2))
            print(sum, max(abs(x2-x1),abs(y2-y2)))
        return sum
    
    def projectionArea(self, grid) -> int:
        hor_sum = 0
        top_sum = 0
        side_sum = 0
        side_max = [list(i) for i in zip(*grid)]
        for i in range(len(grid)):
            hor_sum += max(grid[i])
            top_sum += sum([1 for j in grid[i] if j > 0])
            side_sum += max(side_max[i])


        return hor_sum+top_sum+side_sum
    
    def stoneGame(self, piles) -> bool:
        alias = 0
        bob = 0
        while len(piles) > 1:
            alias += max(piles[1],piles[-1])
            
            
            bob += min(piles[1],piles[-1])
            piles = piles[1:-1]
        return alias > bob
    
    def binarysearch(self,l1,n):
        left = 0
        right = len(l1)-1
        l1 = sorted(l1)
        out = []
        print(l1)
        while left <= right:
            mid = (right+left)//2
            if l1[mid] == n:
                out.append(mid)
                i = mid - 1
                j = mid+1
                while i > 0 and l1[i] == n:
                    out.append(i-1)
                    i -=1
                while j < len(l1) and l1[j] == n:
                    out.append(mid+1)
                    j +=1
                return sorted(out)
            if n > l1[mid]:
                left = mid+1
            else:
                right = mid-1
        return []
    
    def countNegatives(self, grid) -> int:
        def getzeronumber(l1):
            left = 0
            right = len(l1)
            l1 = sorted(l1)
            while left < right:
                mid = (left+right)//2
                if l1[mid] < 0:
                    if mid+1 < len(l1) and l1[mid+1] < 0:
                        left = mid
                    else:
                        return mid
                else:
                    right = mid
            return -1
        sum = 0
        for templist in grid:
            templist = sorted(templist)
            out = getzeronumber(templist)
            sum += out+1
        return sum
    
    def kWeakestRows(self, mat, k: int):
        sol = []
        for i,j in enumerate(mat):
            sol.append([sum(j),i])
        
        print([j for i,j in sorted(sol)[:k]])
    def peakIndexInMountainArray(self, arr) -> int:
        left = 0
        right = len(arr)
        while left <= right:
            mid = (left+right)//2
            print(arr[mid])
            if (mid-1 >=0 and arr[mid-1] < arr[mid]) and (mid+1 <len(arr) and arr[mid+1] < arr[mid]):
                return mid
            if (mid-1 >=0 and arr[mid-1] > arr[mid]):
                right = mid-1
            else:
                left = mid+1


if __name__ == '__main__':
    s = Solution()
   # out = s.hasGroupsSizeX([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3])
   # out = s.simplifiedFractions(4)
    #out = s.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]])
    # out = s.maxCoins([2,4,5])
    #out = s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
   # out = s.projectionArea([[1,2],[3,4]])
   # out = s.stoneGame([3,7,2,3])
    #out = s.countNegatives([[3,2],[1,0]])
    #out = s.binarysearch([81,7,87,77,45,70,4,20,41,8,74,88,71,28,74,41,12,16,99,13,69,34,57,74,76,88,15,1,64,10,28,89,25,12,7,69,81,39,58,79,28,27,7,87,1,66,50,93,30,76,34,22,20,89,35,42,90,22,54,50,10,20,24,44,87],1)
#     out = s.kWeakestRows([[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],3)
    out = s.peakIndexInMountainArray([0,5,10,3,2,1])
    print(out)

        