#roman to integer



# def romantoint(s:str)->int:
#     r2i = {
#     	'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
#     }
#     s = s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX')
#     s = s.replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
#     sum1 = sum(list(map(lambda x:r2i[x],s)))
#     return sum1

# print(romantoint("MCMXCIV"))

def inttoroman(i:int)->str:
    i2r = {
    	1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'
    }
    s=''
    while i !=0:
      
    if i // 1000 > 0 :
        num = i//1000
        i = i - (num*1000)
        s += 'M' * num
    if (i in range(900,999) or i in range(400,499) or i in range(90,99)):
        
    print(i,s)
    
inttoroman(1994)
    