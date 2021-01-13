#! /usr/bin/python3


import hashlib
import json 
import uuid
import datetime
import numpy as np
import time
from nameDump import nameLookup
import Levenshtein as lev



f = open("../data/orig.txt", "r")


with open('../data/thjodDump.txt') as json_file:
    tskra = json.load(json_file)


DEBUG = True
DEBUG = False

def debug(msg):
	if DEBUG:
		print(str(msg))



def lookupTS(bd,nafn):


	match = False
	kyn = None

	if bd in tskra:
		for prsn in tskra[bd]:
			if match == False:
				pp = tskra[bd][prsn]
				tName = pp["name"]

				fuzzLev = lev.ratio(nafn,tName)

				if fuzzLev > 0.9:
					match = True
					kyn = pp["gender"]
					kynMethod = "tskraMatch"
	return match,kyn



def nameMatch(nafn):

	match = False
	kyn = None

	firstName = nafn.split(" ")[0]
	res = nameLookup(firstName)
	if res != None:
		kyn = res[1]
		match = True

	return match,kyn


d = f.read()
d = d.split("\n")
del d[0]


	

nameThing = [ ]
msgcoll = [ ]

for l in d[:-1]:
	raw = l
	c = l.split(";")

	u = uuid.uuid4()
	u = str(u)
	u = u.replace("-","")


	by = c[1].split(".")[2]

	bd = c[1]
	bd = bd.replace(".","")


	hm = c[4].replace(",","")
	hm = int(hm)
	
	fm = c[5].replace("kr","")
	fm = fm.replace(".","")
	fm = int(fm)

	nafn = c[0]





	kyn = None
	match = False
	kynMethod = "No match"



	match,kyn =  lookupTS(bd,nafn)

	if match:
		kynMethod = "tskra"


	if not match:
		match,kyn = nameMatch(nafn)

		if match:
			kynMethod = "name"

		
	if not match:
		l6 = nafn[-6:]
		if l6 == "dóttir":
			kyn = "kvk"
			match = True
			mynmethod = "-dóttir"




	msg = {
                "uuid"                                 :       u,
                "birthYear"                             :       by,
                "city"                                  :       c[3],
                "Heildarlaun a man 2016 f. skatt"       :       hm,
                "Fjarm.tekjur f allt arid 2016"         :       fm,
                "gender"                                :       kyn,
		"match"					:	kynMethod
        }



	if DEBUG:
		if kyn != None:
			print(nafn + "|" + kyn)


	msgcoll.append(msg)

		






outFile = open("../export/launagogn.json","w")
outFile.write(json.dumps(msgcoll, indent=4, sort_keys=True))
outFile.close()


outFile = open("../export/launagogn.dsv","w")
outFile.write("uuid|birthYear|city|Heildarlaun a man 2016 f. skatt|Fjarm.tekjur f allt arid 2016|gender|match\n")

for msg in msgcoll:
	line = ""

	for field in ["uuid","birthYear","city","Heildarlaun a man 2016 f. skatt","Fjarm.tekjur f allt arid 2016","gender","match"]:
		data = msg[field]
		line = line + str(data) + "|"

	line = line[:-1]
	line = line + "\n"

	outFile.write(line)
	






for thing in nameThing:
	#print(thing)
	pass
