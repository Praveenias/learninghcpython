import re
x = re.fullmatch('[0-9]{2,6}-[0-9]{2}-[0-9]{1}','7440-02-0')
x1 = re.fullmatch('[0-9]{2,6}-[0-9]{2}-[0-9]{1}',str('7440‐02‐0'))
print(type('7440‐02‐0'))
print(x)
print(x1)
# if x:
#     print("true")
# else:
#     print("false")
#SELECT * FROM `substances` WHERE id IN (4045,4048,4046,4047,4156,4281,4282,4283,4459,4485,4670,4462,4127);