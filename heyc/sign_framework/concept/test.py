def binarySearch(l,r,list,n):
  
  mid = (l+r)//2
  print(list,list[mid],n)
  if list[mid] == n:
    return mid
  if list[mid] < n:
    return binarySearch(mid,r,list,n)
  else:
    return binarySearch(l,mid,list[:mid],n)

print(binarySearch(0,len([2,4,5]),[2,4,5],5))
  