from datetime import datetime

lifecycle = "active"
rohs = "complaint"

reach = "compliant"

man_stock = 5000
sup_stock = 5000

man_leadtime = 50
sup_leadtime = 50

def life_cycle(status:str) ->str:
  status = status.lower()
  if not status:
    return "unconfirmed"
  if status == "active":
    return "no"
  return "yes"


def rohs_risk(status:str,rohs:str,rohs_date:str)->str:
  rohs_cal = {
    "not-applicable":"NA",
    "unconfirmed":"Unconfirmed",
    "non-compliant":"non-compliant",
    "compliant":"no"
  }
  if status.lower() == "eol":
    return "NA"
  
  if not rohs:
    return "unconfirmed"
  
  if rohs in rohs_cal.keys():
    return rohs_cal[rohs]
  
  if rohs == "compliant-with-exemption":
    if not rohs_date:
      return "No"
    date_object = datetime.strptime(rohs_date, "%Y-%m-%d" )
    if date_object < datetime.today():
      return ""


   
