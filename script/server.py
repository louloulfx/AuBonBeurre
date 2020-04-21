import socket
import threading
import pathlib
import json
import mysql.connector
from mysql.connector import Error


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

    def run(self):
        # print("Connexion de %s:%s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(999999).decode()
        pathFile = pathlib.Path().joinpath(pathlib.Path().absolute(),
                                           '/home/valentinguibert/Documents/Repos/AuBonBeurre/jsonFiles', r)
        with open(str(pathFile), 'rb') as json_file:
            data = json.load(json_file)
            connection = mysql.connector.connect(host='localhost',
                                                 database='devops',
                                                 user='root',
                                                 password='ippon')
            cursor = connection.cursor()
            try:
                for automate in data:
                    sql_insert_automate = """INSERT INTO automates(
                        nb_unite,
                        nb_automate,
                        type,
                        temp_cuve,
                        temp_ext,
                        poids_lait,
                        poids_produit,
                        ph,
                        kplus,
                        nacl,
                        salmonelle,
                        ecoli,
                        listeria,
                        date
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql_insert_automate, (
                        automate['nb_unite'],
                        automate['nb_automate'],
                        automate['type'],
                        automate['temp_cuve'],
                        automate['temp_ext'],
                        automate['poids_lait'],
                        automate['poids_produit'],
                        automate['ph'],
                        automate['kplus'],
                        automate['nacl'],
                        automate['salmonelle'],
                        automate['ecoli'],
                        automate['listeria'],
                        automate['date']
                    ))
                connection.commit()
                print('Donnees inserees')
            finally:
                if cursor != None:
                    cursor.close()
                if connection != None:
                    connection.close()

        self.clientsocket.send('File received by the server'.encode())
        print("Received file from %s:%s" % (self.ip, self.port, ))


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

while True:
    tcpsock.listen(10)
    print("Listening...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
