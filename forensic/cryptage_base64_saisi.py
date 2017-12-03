#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64 
import sys
import os

vide = "Vous devez écrire quelque chose."

print ("")
print ("****************************************")
print ("**                        	      **")
print ("** Base64 Encode.Decode By Bruno      **")
print ("**                                    **")
print ("****************************************")
print ("")
print ("")

def menu():
  
  print('e: Encrypt')
  print('d: Decrypt')
  print('q: Quitter')
  print ("")
   
  choice_var=input(' [>] Que souhaitez vous faire?(e/d/q):')
   
  if(choice_var=='e'):
    print ("")
    __encodez__()
     
  if(choice_var=='d'):
    print ("")
    __decodez__()

  if(choice_var=='q'):
    print('')
    print("Merci d'avoir utilise cet utilitaire.")
    quit()
  else:
    print ("")
    print ("Votre souhait est invalide.")
    print ("")
    menu()

def __encodez__():
  chaine = input('Entrez le texte a encrypter:')
  if(chaine == ""):
    print ("")
    print (vide)
    print ("")    
    __encodez__()
  else:
    encode = base64.b64encode(bytes(chaine, 'utf-8'))
    print ('Votre texte crypté est:')
    print ("")
    print (encode)
    print ("")
    menu()

def __decodez__():
  chaine = input('Entrez la chaine a decrypter:')
  if (chaine == ""):
    print ("")
    print (vide)
    print ("")
    __decodez__()  
  else:
    decode = base64.b64decode(chaine)
    print ('Votre chaine décryptée est:')
    print ("")
    print (decode)
    print ("")
    menu()

menu()
