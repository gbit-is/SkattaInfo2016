import hashlib
import json 
import uuid
import datetime
import numpy as np

DEBUG= True
DEBUG = False

def debug(msg):

	if DEBUG:
		print("Debug: " + str(msg))




f = open("orig.txt", "r")

d = f.read()
d = d.split("\n")
del d[0]



cc = 0


nameThing = [ ]

msgcoll = [ ]

#d = d[:500]
for l in d[:-1]:
	c = l.split(";")

	u = uuid.uuid4()
	u = str(u)
	u = u.replace("-","")

	#print(c)

	bd = c[1].split(".")[2]


	hm = c[4].replace(",","")
	hm = int(hm)
	
	fm = c[5].replace("kr","")
	fm = fm.replace(".","")
	fm = int(fm)

	nafn = c[0]

	kyn = None
		

	kkn = [ "Piotr", "Krzysztof","Pawel","Tomasz","Marcin","Andrzej","Daníel","Adam","Lukasz","Marek","Guðmundur","Michal","Grzegorz","Robert","Mariusz","Jón","Sigurður","Gunnar","Wojciech","Rafal","Dariusz","Kamil","Mateusz","Kristján","Artur","Sebastian","Damian","Stefán","Jakub","Jaroslaw","Martin","Jóhann","Jacek","Miroslaw","David","Ólafur","Maciej"]
	kvkn = [ "Anna", "María" ,"Katarzyna","Maria","Agnieszka","Guðrún","Monika","Kristín","Malgorzata","Joanna","Ewa","Sigríður","Marta","Magdalena","Margrét","Barbara","Natalia","Justyna","Helga","Sigrún","Sigrún","Sandra","Eva","Ingibjörg","Aleksandra"]

	if "son" in nafn:
		kyn = "kk"
	elif "dóttir" in nafn:
		kyn = "kvk"
	else:
		for n in kkn:
			if n in nafn:
				#print ("xxKK: " + nafn)
				kyn = "kk"
		for n in kvkn:
			if n in nafn:
				#print ("xxKvK: " + nafn)
				kyn = "kvk"

		

	if kyn == None:
		#for foo in nafn.split(" "):
			#nameThing.append(foo)
		bleh = nafn.split(" ")
		debug(bleh[0])
		kyn = "nn"

		




	msg = {
		U"uuid"					:	u,
		"birthYear"				:	bd,
		"city"					:	c[3],
		"Heildarlaun a man 2016 f. skatt"	:	hm,
		"Fjarm.tekjur f allt arid 2016"		:	fm,
		"gender"				:	kyn
	}

	msgcoll.append(msg)


	cc = cc + 1





outFile = open("export.json","w")


outFile.write(json.dumps(msgcoll, indent=4, sort_keys=True))
