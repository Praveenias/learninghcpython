A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

m= 4
n = 5
mat=[[0 for i in range(n)] for i in range(m)]
top = left = 0
right= n-1
bottom= m-1
index=0
while left<=right and top<=bottom:
    for i in range(left,right+1):
        mat[top][i] = A[index]
        index +=1
    top +=1
    for i in range(top,bottom+1):
        mat[i][right] = A[index]
        index +=1
    right -=1
    for i in range(right,left-1,-1):
        mat[bottom][i] = A[index]
        index +=1
    bottom -=1
    for i in range(bottom,top-1,-1):
        mat[i][left] = A[index]
        index+=1
    left +=1
#mat[top][left] = A[index]
    #break

for i in mat:
    print(i)