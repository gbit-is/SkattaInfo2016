import hashlib
import json

f = open("../data/thjodskra.txt", "r")

dat = { }

d = f.read()



d = d.split("\n")
del d[-1:]


people = { }


for p in d:
	pp = p.split(":")
	
	kt = pp[2]
	gender = pp[9]
	nafn = pp[4]
	bday = kt[0:6]


	if gender == "1":
		gender = "kk"
	elif gender == "2":
		gender = "kvk"
	elif gender == "3":
		gender = "kk"
	elif gender == "4":
		gender = "kvk"
	else:
		gender = "parsingError_OldThjodskra_DidntReallyHave_AnythingOtherThen_KK_and_kvk"

	ids = kt + gender + nafn 


	index = hashlib.md5(ids.encode('utf-8')).hexdigest()


	person = {
		"name"		:	nafn,
		"gender"	:	gender,
		"kt"		:	kt
	}

	

	if bday not in people:
		people[bday] = { }

	people[bday][index] = person







outFile = open("../data/thjodDump.txt","w")
outFile.write(json.dumps(people, indent=4, sort_keys=True))



