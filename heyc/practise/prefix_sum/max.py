def characterReplacement( s, k):
  maxf = res = 0
  count = {}
  for i in range(len(s)):
      count[s[i]] = count.get(s[i],0)+1
      maxf = max(maxf, count[s[i]])
      print(res,maxf,k)
      if res - maxf < k:
        res += 1
     
      else:
          count[s[i - res]] -= 1
  return res

print(characterReplacement("TTFTTFTT",1))