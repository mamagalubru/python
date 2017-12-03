#!/usr/bin/env python 
# -*- coding: iso-8859-15 -*-

import MySQLdb as SQL;
import datetime;
import smtplib;
import re;

"""
teste la connexion � une base GLPI
et en extrait les �quipements logiciels et mat�riels
� actualiser
"""

# D�finition des variables MySQL
mysqlHost = 'localhost' # � d�finir
mysqlDB = 'glpi' # � d�finir
mysqlUser = 'glpi' # � d�finir
mysqlPasswd = 'mon_mot_de_passe_mysql' # � d�finir

# D�finition des variables du mail
sender = 'no-reply@domain.tdl' # � d�finir
receivers = ['sysadmin@domain.tdl'] # � d�finir
# Attention, la ligne vide � la fin du header est importante, elle fait la s�paration avec le body
header = """From: Support Informatique <%s>
To: <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: [GLPI] Fin de la reservation

""" % (sender, receivers[0])

# Cr�ation d'un dictionnaire pour faire la correspondance entre le type d'item et la base de donn�es associ�e
item_databases_dict = {'Software': 'glpi_softwares', 'NetworkEquipment': 'glpi_networkequipments', 'Computer': 'glpi_computers', 'Peripheral': 'glpi_peripherals', 'ConsumableItem': 'glpi_consumableitems', 'SoftwareLicense': 'glpi_softwarelicenses'}

# On r�cup�re la date du jour : elle va �tre utilis�e dans les calculs
today = datetime.date.today()

# On ouvre la connexion � la base de donn�es et on cr�e le curseur
conn = SQL.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDB)
cursor = conn.cursor()

# On recherche les items dont la reservation arrive � expiration
cursor.execute("SELECT items.itemtype, items.items_id, reservations.comment FROM glpi_reservationitems items, glpi_reservations reservations WHERE (items.id=reservations.reservationitems_id) AND (items.entities_id=7) AND (DATEDIFF(DATE(reservations.end),STR_TO_DATE('%s','%%Y-%%m-%%d')) = 0)" %  (today))
expired_reservations=cursor.fetchall()

for reservation in expired_reservations:
        item_type = reservation[0]
        item_id = reservation[1]
        reservation_comment = reservation[2]
        item_database = item_databases_dict[item_type]
        cursor.execute("SELECT t1.name FROM %s t1 WHERE t1.id=%s" % (item_database,item_id))
        item_name=cursor.fetchone()

        # On commence � construire le mail
        message = header

        # On verifie qu'il y a bien un sender dans le commentaire
        if reservation_comment:
                # On v�rifie que le commentaire correspond bien � une adresse mail
                if re.match('^[a-zA-Z0-1.]+@domain\.tdl',reservation_comment):
                        my_receivers = receivers + [reservation_comment]
                        message += "Emprunteur : %s<br><br>" % (reservation_comment)
                else:
                        my_receivers = receivers
        else:
                my_receivers = receivers

        # On ajout de header au message
        message += "La reservation du mat�riel %s est arriv� � �ch�ance.<br><br>" % (item_name[0])
        message += "Merci de le ramener au service informatique."

        # On envoi le mail
        try:
                mail = smtplib.SMTP('localhost')
                mail.sendmail(sender, my_receivers, message)
                print 'Message envoy�'
        except SMTPException:
                print 'Erreur : le message n\'a pas pu �tre envoy�'

cursor.close()
conn.close()
