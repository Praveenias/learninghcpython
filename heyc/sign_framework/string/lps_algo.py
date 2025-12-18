def compute_lps(pattern):
  lps = [0]* len(pattern)
  j = 0
  i = 1
  while i < len(pattern):
      if pattern[i] == pattern[j]:
          j += 1
          lps[i] = j
          i += 1
      else:
          if j != 0:
              j = lps[j - 1]  # Use previously computed LPS value
          else:
              lps[i] = 0
              i += 1
  return lps

def find_substring(s,pat):
    lps = compute_lps(pat)
    m = len(pat)
    i = j =0
    while i < len(s):
        if s[i] == pat[j]:
            i +=1
            j +=1
        
        if j == m:
            print("pattern found")
            j = lps[j-1]
        elif i < len(s) and s[i]!=pat[j]:
          if j !=0:
              j = lps[j-1]
          else:
              i +=1


        

find_substring("ABABDABACDABABCABAB","ABABCABAB")
