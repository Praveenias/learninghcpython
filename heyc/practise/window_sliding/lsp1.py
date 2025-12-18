

def check_lps(s):
  n = len(s)
  lps = [0] * n
  j =0
  i = 1 
  while i < n:
    if s[i] == s[j]:
      j +=1
      lps[i] = j
      i +=1
    else:
      if j !=0:
        j = lps[j-1]
      lps[i] = 0
      i +=1
  return lps

def kmp_search(text, pattern):
    """Find all occurrences of the pattern in the text using KMP algorithm."""
    n,m = len(text),len(pattern)
    lsp = check_lps(pattern)
    occurerance = []
    j = 0
    for i in range(len(text)):
      while j >0 and pattern[j] != text[i]:
        j = lsp[j-1]
      if text[i] == pattern[j]:
        j +=1
      if j == m:
        occurerance.append(i)
        j = lsp[j-1]
    return occurerance


print(kmp_search('fororfrdofr','for'))
