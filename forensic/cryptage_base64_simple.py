#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-
import base64
"""
teste quelques propriétés pour forensic scientist
expert en criminalistique, ce programme affiche
le code d'un message avant et après cryptage
"""
chin = "Welcome to home"
chout = base64.b64encode(bytes(chin, 'utf-8'))
chinitiale = base64.b64decode(chout)
print ("original:" + repr(chin))
print ("encoded string:" + repr(chout))
print ("decoded string:" + repr(chinitiale))
