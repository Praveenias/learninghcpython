#Function

'''
set or block or organised  of code that can be resued, which performs specific task

 we can call that function whereever we need

input : input paramaters

return : optional

def function_name(input_paramaters):
  #operation
  #return ->optional


function_name(params)


'''

def addition(ip1,ip2=10):
  return ip1+ip2

sum = addition(2,3)
sum = addition(4,6)
aum3 = addition(5)
print(sum)

def prime_number(num1):
  for i in range(2,num1):
    if num1%i == 0:
      return False 
  return True

out = prime_number(3)

# str1 = "A man, in" #n ina, mA
# str2=""

# str_len = len(str1)
# str_len_cpy = str_len
# i=0
# while str_len>i:
#   if str1[i].isalphanum():
#     str2 = str2+str1[str_len_cpy-1]
#   else:
#     str2 = str2+str1[i]
#     str_len_cpy = str_len_cpy-1
#   i=i+1


def add_list(list1):
  return sum(list1)

out = add_list([1,2,3])
print(out)


a=10
b=20
def greatest(a,b):
  if a<b:
    return b
  else:
    return a

out = greatest(10,20)
print(out)


'''

lambda or anonymous function

short or simple or oneline function

lambda aarguments:expression

b = lambda a:a*a
print(b(2)) =>4

map() =>generator output

map(function,iterble)

print(list(map(int,["1","2"])))


reduce
from functools import reduce

reduce(functions,iterables,initializer)

reduce(add,[1,2,3,4,5],10) =>15

filter

filter(function,iterable)

filter(even,[2,4,3,7,5]) => [2,4]

filter fucntion should return True or False


'''


a = [1,2,3,4,5]
  

