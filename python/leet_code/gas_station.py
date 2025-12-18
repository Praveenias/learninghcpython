gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

unit_gas=idx = 0
for i in range(len(gas)):
    #print(unit_gas,cost[gas[idx]-1],gas[idx+1],end=" ")
    unit_gas += gas[i]-cost[i]
    if unit_gas < 0: unit_gas, idx = 0, i+1
print(idx)

# print(unit_gas)