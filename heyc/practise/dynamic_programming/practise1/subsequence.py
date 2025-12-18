def sub(n,arr):
  def subsequence(index,sequ):
    if index == n:
      print(sequ)
      return
    sequ.append(arr[index])
    subsequence(index+1,sequ)
    sequ.pop()
    subsequence(index+1,sequ)
  subsequence(0,[])
sub(3,[1,2,3])

  