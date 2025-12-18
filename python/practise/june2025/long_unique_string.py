def longestKSubstr(s, k):
  maxv = 0
  dict_freq = {}
  left = 0
  for j,i in enumerate(s):
    dict_freq[i] = 1 + dict_freq.get(i,0)
    while len(dict_freq) > k:
      char = s[left]
      dict_freq[char]-=1
      if dict_freq[char] == 0:
        del dict_freq[char]
      left +=1

    if len(dict_freq) == k:
      maxv = max(maxv,j-left+1)
  return maxv
    


print(longestKSubstr("aabacbebebe",3))