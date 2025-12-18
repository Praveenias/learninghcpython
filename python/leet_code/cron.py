a= "* * * * *"
import re

print(re.search("[*]/{1}[1-9]","*/12"))
# a_cron = a.split()
# time = ["minute","hour","day_of_month","month","day_of_week"]
# if len(a_cron) != 5:
#     print("please set valid time")

# a_zip = dict(zip(time,a_cron))

# def validate(a_zip:dict):
#   for key,value in a_zip:
#     if key == "*":
#         continue

    
# for key,value in a_zip:
#     if key == "minute":
#         if key == '*':
#             true +=1
    
# print(a_cron)