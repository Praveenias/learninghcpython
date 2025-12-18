def compute_lps(pattern,k):
  i = 0
  j = len(pattern)
  ans = -1
  while i < j :
    mid = (i - (i-j) )//2
    
    if pattern[mid] == k:
      ans = mid
      j = mid-1

    if pattern[mid] < k :
      i = mid+1
    else:
      j = mid-1
  print(ans)
  return -1
  

print(compute_lps([1,2,2,3,3,3,4,4,4,5,5],3))
