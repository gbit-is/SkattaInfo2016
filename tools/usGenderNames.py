import json 

usNames = { }

with open("../data/usnames.csv") as file:
        f = file.read()
        f = f.split("\n")
        del f[0]
        del f[-1]

        for ff in f:
                ff = ff.split(",")
                n = ff[0]
                kvk = ff[1]
                kk = ff[2]


                d = {
                "kk"    :       kk,
                "kvk"   :       kvk
                }



                usNames[n] = d



outFile = open("../export/usNames.json","w")
outFile.write(json.dumps(usNames, indent=4, sort_keys=True))

