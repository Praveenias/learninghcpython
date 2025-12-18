moves1="LRUD"

moves_dict = {
  "U":"D","D":"U","L":"R","R":"L"
}
def judgeCircle(moves: str) -> bool:
  for i in moves:
    if len(moves)>0:
      print(moves,moves_dict[i])
      moves = moves.replace(i,"")
      if moves_dict[i] in moves:
        print(moves)
        moves = moves.replace(moves_dict[i],"")
        print(moves)
      else:
        return False
    else:
      return True

  print(moves)

print(judgeCircle(moves1))

