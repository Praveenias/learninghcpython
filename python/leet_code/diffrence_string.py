s=""
t="y"
set_s,set_t = {},{}
for i in set(s):
    set_s[i] = s.count(i)
for j in set(t):
    set_t[j] = t.count(j)
    if j not in set_s:
       set_s[j] = 0
for key,val in set_t.items():
  if val != set_s[key]:
     print(key)
  #print(key,val,set_s[key])
#print(set(t)-set(s))
# min_sort = s if len(s)<len(t) else t

# min_string = max(s,t)


# print(max(s,t)[len(min_sort):],min_sort)