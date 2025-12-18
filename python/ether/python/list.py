#list
'''
ordered collection of item

[]
[1,2,3,4,5]
["abc",10,False,1.0]


l1=["a",2,3,True]
l1[1] =>2

l1[3]=False
print(l1)

l1.append(6)
l1.remove(4)

len(l1)

l1=[1,2.3]
l2=[4,5,6]
l1+l2

l1.index(4)
l1.count(4)
min()
max()
sum()
l1.pop()
l1.sort()
l1.reverse()
l1.insert(1,5)


list slicing
orginal_lsit[srart_index:end_index:step]
l1=[1,2,3,4,5]
l1[:4] => [1,2,3,4]
l1[2:4] = > [3,4]
l1[::2] =>[1,3,5]
l1[::-1] => [5,4,3,2,1]


__________________________________________________

Tuples:


Tuples is an immutable list of values

comma seperated values, start and end with ( and )

tuple_1 = (1,2,3,4,5)+(2.3)

tuples are immutable.. tuples values cannot be edited

max()
min()

tlist to tuple : tuple()



______________________________________________________


set

unorered collection of uniqueu elements set()

set_1 = {1,2,3,4}

set_2= {2,3,7,8}

set_3 = {1,2}

selt1.intersection(set2) => {2,3}

set1.union(set2)  =>{1,2,3,4,7,8}

set1.difference(set2) => {1,4}

set2.difference(set1) => {7,8}

set_3.issubset(set_1) => True check each element in set3 in set1

set_1.issuperset(set3) =>True check each element in set3 in set1


set1.add(5)



_______________________________________________________________________


Dictionary


collection of Key value pair in python

by refereing key we can retrive and store an element


dict1 = {key:value}

dict = {"name":"praveen","age":20}

dict["age"]

dict["address"] = "cbe"

del dict["age"]

for i in dict:
  print(i,dict[i])


dict1.keys() => [ "name","age"]

dict1.values() => ["praveen",20]

dict.items() => [("name","praveen"),("age",20))]














'''
