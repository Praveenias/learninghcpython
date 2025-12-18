def countop(s):
    openbrancket = 0
    closebracket = 0
    
    # s = '}{{}}{{{'
    stack = []
    for i in s:
      if i  == '{':
        openbrancket +=1
        stack.append(i)
      else:
        if stack and stack[-1] in stack:
          stack.pop()
          closebracket -=1
          openbrancket -=1
          # continue
        closebracket +=1
      #print(openbrancket,closebracket)
    print(openbrancket,closebracket,stack)
    if (openbrancket + closebracket) % 2 == 0:
      return len(stack)
    else:
      return -1
#print(countop("}}}}}}{}{}}}{{}}}}{}}{{{}{}{}{}}{{{{}}}{}}"))  #7
print(countop("}{{}}{{{"))  #7

    

# print(len(stack))
