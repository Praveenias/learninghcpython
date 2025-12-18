mat = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8]
    ]

top = left = 0
right = len(mat[0])-1
bottom = len(mat)-1
print(top,left,bottom,right)
while left <= right and top<=bottom:
    for i in range(left,right+1):
        print(mat[top][i],end=" ")
    top +=1
    #print(top,left,bottom,right)
    for i in range(top,bottom+1):
        print(mat[i][right],end=" ")
    right -=1
    for i in range(right,left-1,-1):
        print(mat[bottom][i],end=" ")
    bottom -=1
    for i in range(bottom,top-1,-1):
        print(mat[i][left],end=" ")
    left +=1
#print(mat[top][left])
    #print(top,left,bottom,right)

