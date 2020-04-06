import json
import calendar
import time
import random
import os 

id_unite = [os.getenv('UNITE')]
starttime = time.time()
id_automate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
id_type_automate = ["0", "1", "2", "3", "4", "5",
                    "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
date = calendar.timegm(time.gmtime())

while True:

    for x in id_unite:
        print(x)
        name = "paramunite_"+str(x)+"_"+str(date)+".json"
        data = []
        date = calendar.timegm(time.gmtime())

        for y in id_automate:
            automate = {
                "Numéro d'unité": x,
                "Numéro d'automate": y,
                "Type d'automate": '0X000BA2'+random.choice(id_type_automate),
                "Température cuve": round(random.uniform(2.5, 4), 1),
                "Température extérieure": random.randrange(8, 14, 1),
                "Poids du lait en cuve": random.randrange(3512, 4607, 1),
                "Poids du produit fini réalisé": 4607-random.randrange(3512, 4607, 1),
                "Mesure pH": round(random.uniform(6.8, 7.2), 1),
                "Mesure K+": random.randrange(35, 47, 1),
                "concentration de NaCl": round(random.uniform(1, 1.7), 1),
                "Niveau bactérien salmonelle": random.randrange(17, 37, 1),
                "Niveau bactérien E-coli": random.randrange(35, 49, 1),
                "Niveau bactérien Listéria": random.randrange(28, 54, 1),
                "Date": time.strftime("%d/%m/%Y %H:%M:%S")
            }
            data.append(automate)

        with open('jsonFiles/'+name, "w") as file:
            json.dump(data, file)

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
