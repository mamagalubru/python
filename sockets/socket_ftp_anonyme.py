#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import socket

"""
teste quelques propri�t�s pour forensic scientist : expert en criminalistique
ce programme effectue une connexion anonyme sur un site ftp
"""

host = "ftp.ibiblio.org"
port = 21

# cr�ation de l'objet socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
   # connexion et liaison
   s.connect((host,port))
   # r�ception des donn�es d'invite
   data = s.recv(1204)
   print (data)
   # envoi de l'identifiant de connexion
   s.send(bytes("USER anonymous\r\n",'UTF-8'))
   # r�ception de la r�ponse
   data = s.recv(1204)
   print (data)
   # envoi du mot de passe
   s.send(bytes("PASS test@free.fr\r\n",'UTF-8'))
   # r�ception de la r�ponse
   data = s.recv(1204)
   print (data)
   # envoi de la commande pwd
   # s.send(bytes("PWD\r\n",'UTF-8'))
   # r�ception de la r�ponse
   # data = s.recv(1204)
   # print (data)
   # sortie propre
   s.send(bytes("QUIT\r\n",'UTF-8'))
   s.close()

except socket.error as e:
   print("Cannot connect to " + host)
   print(" On port: " + str(port))
   print(e)
