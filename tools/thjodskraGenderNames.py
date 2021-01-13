import json


with open('../data/thjodDump.txt') as json_file:
    tskra = json.load(json_file)


coll = { }

for entry in tskra:
	data=tskra[entry]

	for p in data:
		pp = data[p]
	
		name = pp["name"]
		gender = pp["gender"]
		firstName = name.split(" ")[0]
		
		if firstName in coll:
			pass
		else:
			coll[firstName] = { }
			coll[firstName]["kk"] = 0
			coll[firstName]["kvk"] = 0

			
		c = coll[firstName][gender]
		c = c + 1
		coll[firstName][gender] = c



outFile = open("../export/genderedNames.json","w")
outFile.write(json.dumps(coll, indent=4, sort_keys=True))

