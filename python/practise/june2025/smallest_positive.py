def missingNumber(arr):
        n = len(arr)
        arr1 = [-1] * len(arr)
        for i in arr:
            if i < n and i > 0:
              arr1[i] = 1
        for i in range(1,n):
             if arr1[i] == -1:
                  return i

print(missingNumber([2, -3, 4, 1, 1, 7]))
print(missingNumber([5, 3, 2, 5, 1]))
print(missingNumber([-8, 0, -1, -4, -3]))


