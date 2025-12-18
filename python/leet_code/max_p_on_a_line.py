l1=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
l2=[sorted(i) for i in l1]
l3=[]
for i in l2:
    if i not in l3:
        l3.append(i)
print(l3,len(l3))
