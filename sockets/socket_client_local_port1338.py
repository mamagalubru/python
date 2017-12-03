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
   s.connect((host,port))
   # boucle de réception de la réponse
   while 1:
      data = str(s.recv(1024))
      if data == "fin":
         break
      print ("Serveur > " + data)
      mot = input ("Entrez votre mot (fin pour quitter) : ")
      s.send(bytes(mot,'UTF-8'))
   s.close()

except socket.error as e:
   print("Cannot connect to " + host)
   print(" On port: " + str(port))
   print(e)
