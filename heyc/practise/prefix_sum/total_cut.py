a=[2, 6,10, 2, 8]
k = 5
N=5
prefix_max = [2]*N
suffix_min = [2]*N

for i in range(1,len(a)):
  prefix_max[i] = max(prefix_max[i - 1], a[i])
for i in range(N - 2, -1, -1):
  suffix_min[i] = min(suffix_min[i + 1], a[i])

count = 0
for i in range(N-1):
  if prefix_max[i] + suffix_min[i+1] >=N:
    count +=1

print(count)
print(suffix_min,prefix_max)
