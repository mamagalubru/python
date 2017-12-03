#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import sys
import subprocess

"""
teste quelques propriétés pour forensic scientist : expert en criminalistique
ce programme effectue un ping sur une adresse saisie
"""

ip = input("Veuillez entrer une adresse IP : \n")

try:
   ipi = ip.split(".")
   for i in ipi:
      int(i)
except:
   print ("Mauvaise adresse IP\n")
   sys.exit()

ipi.pop()
ipf = ".".join(ipi)

monos = sys.platform
print(monos)
monoption = '-n' if monos != 'win32' else ''
print(monoption)

for i in range(1,255):
   machine = ipf + "." + str(i)
   resu = subprocess.call(['ping', '-w', '2', machine])
   if resu == 0:
      print (" la machine IP %s répond " % machine)
   else:
      print (" la machine IP %s ne répond pas" % machine)
