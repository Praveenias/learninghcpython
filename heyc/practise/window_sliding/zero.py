arr = [7 ,532, 16, 932, 99, 2, 4, 8, 12]

def MostFrequent():
      s = ".*.*..**.*"
      k = 2
      damaged = 0
      left = 0
      maxv = 0
      for r in range(len(s)):
          if s[r] == '.':
               damaged +=1
          
          while damaged > k:
            if s[left] == '.':
                  damaged -=1
            left +=1
          maxv = max(maxv,r-left+1)
      print(maxv)  
          


print(MostFrequent())