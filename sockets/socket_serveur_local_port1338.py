#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import socket

"""
teste quelques propriétés pour forensic scientist : expert en criminalistique
ce programme sert les communications client sur le port 1338
"""

host = "192.168.1.11"
port = 1338

# création de l'objet socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
   # connexion et liaison
   s.bind((host,port))
   # écoute
   print ("Allo > ")
   s.listen(1)
   # réception des données du client
   client,adresse = s.accept()
   print (adresse)
   print (client.getpeername)
   # envoi bonjour au client
   client.send(bytes("Bonjour, je suis bruno1338, entrez un mot ou fin\r\n",'UTF-8'))
   # boucle de réception de la réponse
   while 1:
      data = str(client.recv(1024))
      if data == "fin":
         break
      print ("Client > " + data)
      client.send(bytes("Serveur en attente de mot > \r\n",'UTF-8'))
   client.close()
   s.close()

except socket.error as e:
   print("Cannot connect to " + host)
   print(" On port: " + str(port))
   print(e)
