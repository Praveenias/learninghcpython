mat = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]

top = left = 0
right= len(mat[0])-1
bottom= len(mat)-1

prev=mat[0][0]
while left<=right and top<=bottom:
    for i in range(left,right+1):
        next= mat[top][i]
        mat[top][i] = prev
        prev= next
    top +=1
    
    for i in range(top,bottom+1):
        next = mat[i][right]
        mat[i][right] = prev
        prev= next

    right -=1
    for i in range(right,left-1,-1):
        next = mat[bottom][i]
        mat[bottom][i] = prev
        prev= next
    bottom -=1
    for i in range(bottom,top-1,-1):
        next = mat[i][left]
        mat[i][left] = prev
        prev= next
    left +=1
mat[0][0] = prev
    #break

for i in mat:
    print(i)
