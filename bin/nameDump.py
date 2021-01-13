import json



minMatches = 7
minPercent = 3

with open('../export/genderedNames.json') as json_file:
	nameList = json.load(json_file)


with open("../export/usNames.json") as json_file:
	usNames = json.load(json_file)

		



	
	


def usLookup(name):
	if name in usNames:
		#print("+ " + name)
		nameData = usNames[name]
		
		gender, otherPerc = nameDataParse(nameData)
	
		if gender != None:
			return True, gender
		else:
			return False,None
	
	else:
		return False,None

def nameDataParse(nameData):

	kk = int(nameData["kk"])
	kvk = int(nameData["kvk"])
	nameCount = kk + kvk


	if nameCount > minMatches:
		if kk > kvk:
			gender = "kk"
			otherPerc = (kvk/kk) * 100


		if kk < kvk:
			gender = "kvk"
			otherPerc = (kk/kvk) * 100
		if kk == kvk:
			gender = None
			otherPerc = 50

	else:
		otherPerc = 404
		gender = None

	return gender,otherPerc


def nameLookup(name):

	if name in nameList:
		#print("in namelist")
		nameData = nameList[name]
		
		gender,otherPerc = nameDataParse(nameData)
		

		if otherPerc > minPercent:
			#print("low perc")
			usLookup(name)
			

		return True, gender
	else:
		#print("not in list")
		usLookup(name)





