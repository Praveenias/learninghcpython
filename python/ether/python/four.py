from functools import reduce

print(reduce(lambda x,y:x*y,[-9,8,2,5]))

# str1='abcdefghijklmnopqrstuvwxyz'
# print(str1)
# #e=5
# #loop(5)range(5)

# def addition(a,b):
#     return a+b

# print(addition(2,3))


l1=[1,2,3,1,2]

flag=True
for i in l1:
    if l1.count(i) >1:
        flag = False
        print(i)
if flag:
    print(-1)

class One: 
    def In_one():
        print("in module 1")


def In_one_1():
  print("in module 1")


    