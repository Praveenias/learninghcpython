nums = [0,0,0,0,1]
goal = 2
count = 0
prefix_sum = {0:1}
suma = 0

for j in range(len(nums)):
    suma +=nums[j]
    if suma >= goal:
        count += prefix_sum[suma]
    prefix_sum[suma] = prefix_sum.get(suma,0) +1
print(count)
        



print(count)

