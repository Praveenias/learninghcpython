
try:
  # a=10
  # b=0
  # c=a/b
  print("hit")
  raise Exception("intensinally error raised")

# except ZeroDivisionError:
#   print("zero division erro")

# except ValueError:
#   print("value error ")

except NameError:
  print("name error")

except Exception as e:
  print("in exception",e)

# else:
#   print(e)

finally:
  print("always executable")


# If any error occured how we are going to handle runtime error .

#it prevent crashing program and give reasonable error defination

#finally code block will execute by default.. if error occured or not occured

# raise i found an error intensionnlay i need to exit from it then i can use raise Exception()