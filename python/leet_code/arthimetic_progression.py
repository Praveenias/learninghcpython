arr=[3,5,1]
arr = sorted(arr,reverse=True)
print(arr)
diff = arr[0]-arr[1]
for i in range(1,len(arr)-1):
    num = arr[i]-arr[i+1]
    print(num)
    if num!=diff:
        print(False)
print(True)