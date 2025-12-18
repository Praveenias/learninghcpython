from xmlrpc.client import Boolean


l1={'{':'}','[':']','(':')'}
#input = input()

def check_paratheses(input:str)->Boolean:
    valid=[]
    for i in input:

        if i in l1.keys():
            valid.append(i)
            continue
        if valid:
            if l1[valid[-1]]==i:
                valid.pop()
            else:
                return False
        else:return False
        print(valid)
    return True

print(check_paratheses("{{()}()}[]"))
         