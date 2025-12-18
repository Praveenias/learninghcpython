class Praveen:
    def __init__(self,name):
      self.name = name
      self.age = age
        
    def welcome(self):
      print(f"welcome {self.name}")

prav_ob = Praveen("praveen")
prav_ob.welcome()

abc_obj = Praveen("abc")
abc_obj.welcome()

class Human:
  a = 10
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def eat_style(self,eat):
    print(f"{self.name} eating style is {eat}")

  def __str__(self) -> str:
    return "Hi"

  
class PraveeenList(list):
  pass

praveen = Human("praveen",24)
praveen.eat_style("veg")

saravana = Human("Saravana",23)
saravana.eat_style("non veg")
print(Human.a)


    