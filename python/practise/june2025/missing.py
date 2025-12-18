def missingNum( arr):
        n = len(arr)
        temp = [-1]* (n+1)
        for i in arr:
            temp[i-1] = i
        for i,j in enumerate(temp):
            if j ==-1:
                return i+1
        return n+1
print(missingNum([1, 2, 3, 5]))