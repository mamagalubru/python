#! /usr/bin/python
# -*-

intab = b"abcdefghijklmnopqrstuvwxyz"
outtab = b"nopqrstuvwxyzabcdefghijklm"
transtab = bytes.maketrans(intab, outtab)

"""
teste quelques propriétés pour forensic scientist : expert en criminalistique
ce programme affiche le code d'un message après cryptage simple en rot13
"""

chin = "WelcomeToHome"
chout = chin.translate(transtab)
chinitiale = chout.translate(transtab)
print ("original:" + repr(chin))
print ("encoded string:" + repr(chout))
print ("decoded string:" + repr(chinitiale))

