mat = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
        [4, 5, 6, 7, 8],
        [5, 6, 7, 8, 9]
    ]

for i in range(len(mat)):
    print(mat[i][i])
    for j in range(i):
        print (mat[i][j],end=" ")
    break