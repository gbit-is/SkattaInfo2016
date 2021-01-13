# SkattaInfo2016 - export 


## genderedNames.json
gagnasett sem varð til við þetta verkefni, öll nöfn úr Íslenskri þjóðskrá 1997 og hversu margir KK og KVK hétu það (sem fyrsta nafn)

## usNames.json
stórt gagnasett af kyngreindum nöfun byggð á ../data/usnames.csv.gz

## launagogn.dsv / launagogn.json.gz
Hérna er aðal stöffið   
launagogn.dsv - delimiter seperated á "|" 
launagogn.json.gz - standard json format compressað með gzip, 73Mb uncompressed

### fields:
	uuid				:	randomly generated kóði (generated per keyrsla, ekki reversable)
	birthYear			:	2 stafa fæðingarár
	city				:	Borgin sem manneskjan býr í 
	Heildarlaun a man 2016 f. skatt	:	Heildarlaun per mánuð
	Fjarm.tekjur f allt arid 2016	:	fjarmagns tekur fyrir allt árið 2016, mögulega gallaðar. treysti þeim ekki jafn vel og heildarlaun
	gender				:	Kyn, kk/kvk/None ( 84% matchað úr þjóðskrá á kennitölu, 13% útfrá nafni, 3% hafði ekki nægilegar upplýsingar)
	match				:	Hvernig kyn var fundið, hvort það var úr þjóðskrá á kennitölu, nafni eða ekki náð að finna kynið
