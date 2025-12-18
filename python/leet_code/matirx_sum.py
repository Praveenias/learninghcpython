mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
h_sum = 0
for i in range(len(mat)):
  h_sum += mat[i][i]

d_sum = 0

mat_len = len(mat)-1
for j in range(len(mat)):
  if j==mat_len:
    mat_len -=1
    continue
  d_sum += mat[j][mat_len]
  mat_len -=1

print(h_sum+d_sum)