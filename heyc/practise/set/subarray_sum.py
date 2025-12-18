def find_subarray_sum(arr, n, sum):
  hash_map = {0:1}
  sumk = 0
  count = 0
  for i in arr:
    sumk +=i
    if sumk-sum in hash_map:
      print(i,sumk-sum,sumk,hash_map)
      count +=hash_map[sumk-sum]
    hash_map[sumk] = hash_map.get(sumk,0) +1
  return count


print(find_subarray_sum([-4 ,4 ,3 ,3, 8, -2],6,6))
