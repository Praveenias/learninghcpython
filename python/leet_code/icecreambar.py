cost =[1,6,3,1,2,5]
coins=20
cost.sort()
res=0
for i in cost:
    if i<=coins:
        res+=1
        coins -=i
    else:
        break
    print(i,coins)
print(res)
