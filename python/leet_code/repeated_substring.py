#s="ababab"
#s="abab"
s="ababab"
#s="aba"
# print(s[:1],s[:-1])
for i in range(1,len(s)//2):
    #print(i)
    print(s[0:i+1])
    print(s[0:i+1]*(len(s)//i))

# sub_str = s

# len_sub_str=len(s)//2
# i=2
# while(len_sub_str>0):
#   sub_str = sub_str[:len_sub_str]
#   print(sub_str)
#   if sub_str*i == s:
#     print(True)
#     #break
#   len_sub_str = len(sub_str)//2
#   i=i*2
#   #break
  
# print(False)
  
  


# for i in range(len(s)//2):
  