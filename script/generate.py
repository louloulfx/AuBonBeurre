import json
import calendar
import time
import random
import os
import socket
import sys

# id_unite = os.getenv('UNITE')

# Set number of 'unites' and 'automates'
nb_unite = 5
nb_automate = 10

# Set 'automate' types available
id_type_automate = ["0", "1", "2", "3", "4", "5",
                    "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# Set date
starttime = time.time()
date = calendar.timegm(time.gmtime())

while True:

    for x in range(1, nb_unite + 1):
        print('\nCreating file for "unite %s"' % x)
        name = "paramunite_"+str(x)+"_"+str(date)+".json"
        data = []
        date = calendar.timegm(time.gmtime())

        for y in range(1, nb_automate + 1):
            automate = {
                "nb_unite": x,
                "nb_automate": y,
                "type": '0X000BA2'+random.choice(id_type_automate),
                "temp_cuve": round(random.uniform(2.5, 4), 1),
                "temp_ext": random.randrange(8, 14, 1),
                "poids_lait": random.randrange(3512, 4607, 1),
                "poids_produit": 4607-random.randrange(3512, 4607, 1),
                "ph": round(random.uniform(6.8, 7.2), 1),
                "kplus": random.randrange(35, 47, 1),
                "nacl": round(random.uniform(1, 1.7), 1),
                "salmonelle": random.randrange(17, 37, 1),
                "ecoli": random.randrange(35, 49, 1),
                "listeria": random.randrange(28, 54, 1),
                "date": time.strftime("%d/%m/%Y %H:%M:%S")
            }
            data.append(automate)

        with open('jsonFiles/'+name, "w") as file:
            json.dump(data, file)

        print('File %s created' % name)

        print('Sending File to server')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("", 1111))
        s.send(name.encode())
        response = s.recv(100).decode()
        print(response)

    print("\nNext files will be sent in 60 seconds")

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
