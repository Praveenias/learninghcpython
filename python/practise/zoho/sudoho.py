def solve(board):
  rows = [set() for i in range(9)]
  columns = [set() for j in range(9)]
  dia = [set() for k in range(9)]

  def checkvalid(row,col,num):
    if num in rows[row] or num in columns[col]:
      return False

    start = 3* (row//3)
    return True

  for row in range(9):
    for col in range(9):
      if board[row][col] == '.':
        for i in '123456789':
          if checkvalid(row,col,i):
            board[row][col] = i
            if checkvalid():
              return True
            board[row][col] = '.'
        return False
  return True







solve([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
