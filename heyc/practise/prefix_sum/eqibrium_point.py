a =[5, 4, 3, 2, 1]
total_sum = sum(a)

prefix_sum = 0

for i in range(len(a)):
  if total_sum-prefix_sum-a[i] == prefix_sum:
    print(i)
  prefix_sum +=a[i]
