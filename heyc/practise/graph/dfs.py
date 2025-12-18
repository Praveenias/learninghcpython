def dfs(n):
  mat = [[0]*n for i in range(n)]
  mat[0][1] = 1
  mat[0][3] = 1
  mat[1][0] = 1
  mat[1][2] = 1
  mat[2][1] = 1
  mat[2][3] = 1
  mat[3][0] = 1
  mat[3][2] = 1
  mat[5][4] = 1
  mat[4][5] = 1
  # visited = [False]*n
  traversehelper(mat)

def traversehelper(mat):
  n = len(mat)
  visited = [False]*n
  for i in range(n):
    if visited[i] == False:
      traverse(mat,i,visited)



def traverse(mat,sn,visited):
  visited[sn] = True
  print(sn,end = " ")
  leng = len(mat[sn])
  for i in range(leng):
    if mat[sn][i] ==1 and not visited[i]:
      traverse(mat,i,visited)


dfs(6)