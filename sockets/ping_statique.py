#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import sys
import subprocess
 
def execute(*machines):
   for machine in machines:
      result = subprocess.call(['ping', '-w', '2', machine],stdout=subprocess.DEVNULL)
      if result == 0:
         print("Address {} OK".format(machine))
      else:
         print("Address {} no response".format(machine))
 
execute('192.168.1.11', '192.168.1.15', '192.168.1.254')
