

# ATH: 
## kynjagreiningarnar þarna eru ekki alveg nógu góðar 
### en ég er langt komin með að endurskrifa þann hluta, nákvæmara gagnasett ætti að birtast á næstu dögum

.

# SkattaInfo2016

2017 gerði einhver dúddi heimasíðu með skattaupplýsingum allra Íslendinga að sjálfsögðu fékk ég gögnin í hendurnar nokkrum dögum seinna, ákvað að loksins birta nafnlausa úttekt á þesum ásamt kóðanum um hvernig ég gerði gögnin nafnlaus

# Skjöl:

## export.7z 
Json export af gögnunum, compressuð af því að github leyfði mér ekki að uploada þeim hráum 

## orig.txt
Kjaftæðisdæmi um línur af source gögnunum sem ég fékk

## parse.py
dirty python skrifta sem ég notaði til að parse-a þetta


# Fields:
Fjarm.tekjur f allt arid 2016 :            Fjármagnstekjur fyrir allt árið 2016   
Heildarlaun a man 2016 f. skatt:           (áætluð?) Heildarlaun á mánuði 2016 fyrir skatt    
birthYear :                                2 stafa tala fyrir fæðingarár, engin munur á á að fæðast 1915 og 2015    
city :                                     Bæjarfélag, frekar en fullt heimilisfang   
gender :                                   gróf áætluð kyn, "-dóttir" == kvk, "-son" == "kk, svo öll nöfn sem komu 100+ oft fyrir fengu sérreglu, önnur nöfn fengu NN sem kyn   
uuid :                                     GUID generated per keyrslu, ekkert hash eða sum, pure GUID til að geta vitnað í stakar færslur    
