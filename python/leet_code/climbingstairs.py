#Dyanamic programming
n=5
if n<=3:
    print(n)
a=1
b=1
for i in range(n):
    a,b=b,a+b
    print(a,b)
print(a)
#1,1,1,1,1
#2,2,1
#1,2,2
#2,1,2
#1,1,1,2
#2,1,1,1
#1,2,1,1
#1,1,2,1