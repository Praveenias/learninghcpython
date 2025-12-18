
points=[[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
#[[1, 6], [2, 8], [7, 12], [10, 16]]
points.sort(key=lambda x:x[1])
print(points)
cur,end =1,points[0][1]
for s,e in points:
    print(s,e)
    if end<s:
        end=e
        cur+=1
print(cur)






# points.sort()
# print(points)
# points.sort(key=lambda x:x[1])
# res, curEnd = 1, points[0][1]
# for start,end in points:
#     if start>curEnd:
#         curEnd = end
#         res += 1
# print(res)