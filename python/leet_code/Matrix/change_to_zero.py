mat = [[ 1 , 1 , 0 , 1 , 1 ],
    [ 1,  1,  1 , 1  ,1 ],
    [ 1 , 1 , 1 , 0 , 1 ],
    [ 1 , 1 , 1 , 1 , 1 ],
    [ 0 , 1 , 1 , 1,  1 ]]

for i in range(len(mat)):
    print(mat[i])
    if 0 in i:
        change_matrix()
print(mat)



