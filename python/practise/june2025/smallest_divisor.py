import math
def smallestDivisor(arr, k):
        def canceil(n):
            cnt = 0
            for i in arr:
                cnt += math.ceil(i/n)
            return cnt <=k
        l,r = 1,max(arr)
        res =r
        while l <r:
            mid = (l+r)//2
            print(mid,canceil(mid),l,r)
            if canceil(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res

print(smallestDivisor([21,23],5))