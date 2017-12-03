#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
    teste quelques propriétés de chaines de caractères
"""

FRED = "fred"
print(FRED)

FREDO = 'elle est rose'
print(FREDO)

FREDI = ''' je suis rouge et bleu
et vert et noir à la fois '''
print(FREDI)

FREDE = ''' (triple apostrophe) \
il dit "Qu'il est génant d'être étourdi et noir à la fois" '''
print(FREDE)

FREDU = ' (échappement via antislash) \
il dit \"Qu\'il est génant d\'être étourdi et noir à la fois\" '
print(FREDU)

FREDY = " (échappement via antislash) \
il dit \"Qu\'il est génant d\'être étourdi et noir à la fois\" "
print(FREDY)

SCORE = 1000
MESSAGE = 'tu as obtenu %s points '
print(MESSAGE)
print(MESSAGE % SCORE)

NOMBRES = 'que dit un %s à un %s ? Jolie ceinture !'
print(NOMBRES)
print(NOMBRES % (0, 8))

for i in range(1, 5):
    print(i * 'smack ')
