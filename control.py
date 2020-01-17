

import psutil
import requests, json

url = "http://192.168.0.101/zabpy/index.php"
agent = 4
disk = psutil.disk_usage('/')

spazio_totale = disk.total/1024**3
spazio_libero = disk.free/1024**3
spazio_usato = disk.used/1024**3
percentuale_disco = disk.percent
percentuale_disco = (int(percentuale_disco))

spazio_totale = round(spazio_totale, 2)
spazio_libero = round(spazio_libero, 2)
spazio_usato = round(spazio_usato, 2)

spazio_totale = "{} Gb".format(spazio_totale)
spazio_libero = "{} Gb".format(spazio_libero)
spazio_usato = "{} Gb".format(spazio_usato)

if percentuale_disco <  80:
	 allerta_status_disco = 'OK'
else:
	allerta_status_disco = 'IN ESAURIMENTO'



################################################
#######|#########################################
#######|########################################
#######|#########################################
#################################################
mem = psutil.virtual_memory()

ram_totale = mem.total/1024**3
ram_usata = mem.used/1024**3

ram_totale = round(ram_totale, 2)
ram_usata = round(ram_usata, 2)

ram_totale = "{} Gb".format(ram_totale)
ram_usata = "{} Gb".format(ram_usata)



#####rosa è la chiave quello dopo è il valore
data = {'spazio_totale': spazio_totale, 'spazio_libero': spazio_libero, 'spazio_usato': spazio_usato,'percentuale_disco': percentuale_disco,'allerta_status_disco': allerta_status_disco, 'ram_totale': ram_totale,'ram_usata': ram_usata} 
params = {'id_agent': agent, 'log': json.dumps(data)} 

r = requests.post(url = url, params = params)

print(r.text)


