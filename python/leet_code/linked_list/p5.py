def validparenthesis(s):
#   open_bracket="{[("
#   list1=["[]","{}","()"]
#   if (s.count("(")==s.count(")")) and (s.count("[")==s.count("]")) and (s.count("{")==s.count("}")):
#         for i in range(0,len(s)-1):
#             if i not in ["[","]","{","}","(",")"]:
#               s.replace(s[i],"",1)
#               continue
#             i=0
#             for j in range(i+1,len(s)):
#                 if s[i] in open_bracket and s[i]+s[j] in list1:
#                     s=s.replace(s[i],"",1).replace(s[j],"",1)
#                     break
#                 elif s[i] not in open_bracket:
#                     return "error"
#   print(s)
#   if  len(s)==0:
#     return True
#   return False
  parentesis_dict = {"{":"}","[":"]","(":")"}
  out=[]
  for i in s:
    if i in parentesis_dict.keys():
        



s="[567]"
print(validparenthesis(s))
