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
    if not visited[i]:
      traverse(mat,i,visited)

def traverse(mat,i,visited):
  Queue = []
  Queue.append(i)
  visited[i] = True
  while Queue:
    num = Queue.pop(0)
    print(num,end = ' ')
    for j in range(len(mat[num])):
      if mat[num][j] == 1 and not visited[i]:
        Queue.append(j)
        visited[j] = True
        traverse(mat,j,visited)


dfs(6)