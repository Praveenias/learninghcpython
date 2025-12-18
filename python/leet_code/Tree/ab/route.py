
#route=["trichy","tirunelveli"]
#stops=["chennai","viluppuram","trichy"] #331
#stops=["karur","trichy","viluppuram"] #248
#stops=["trichy","madurai","tirunelveli"] #309
#stops=["chennai","viluppuram","trichy","karur"] #414
#stops=["chennai","viluppuram","trichy","madurai","tirunelveli"]
stops=["tenkasi","madurai","trichy","viluppuram","chennai"]

routes={"chennai":["viluppuram",166],"viluppuram":["trichy",165],"trichy":["madurai",138],
	"madurai":["tirunelveli",171],"tirunelveli":["kanyakumari",85],
	"karur":["trichy",83],"madurai":["tenkasi",100]}
updated_d={}
for k,j in routes.items():
	str1 = ''.join(sorted(k+j[0],key=str.lower))
	updated_d[str1]=j[-1]

#print(updated_d)

def modifystr(str2):
	return ''.join(sorted(str2,key=str.lower))

distance = 0
for stop in range(len(stops)-1):
	rout = modifystr(stops[stop]+stops[stop+1])
	if modifystr(rout) in updated_d.keys():
		distance+=updated_d[rout]
	else:
		print("no such route")
		break
print(distance)
