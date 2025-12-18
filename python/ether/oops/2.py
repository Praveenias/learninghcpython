

class Pranetclass:

    @staticmethod
    def parent_method(self):
        print("iam from parent class")

class Childclass(Pranetclass):
    def __init__(self,num1) -> None:
        self.num1= num1

    def __child_method(self):
        print("iam from child class")

chld_obj = Childclass(20)
Pranetclass.parent_method()
print(chld_obj.num1)
print(chld_obj.child_method())
print(chld_obj.parent_method())

'''
1. Single Inheritance

Parent

child1 child2

2. Multiple I heritance

Parent1,parent2

child()parent1,parent2

3.Multilevel Inheritance
Grantparent

parent(grantparent)

child(parent)

4. Heirarical Inhertaiace

#many child class derived its common behavior from a single parent class

5.Hybrid iNHERITANCE
Combination of SIngle,multiple and multilevel
'''