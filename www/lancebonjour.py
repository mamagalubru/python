#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

# on lance le programme bonjour en cliquant

print('Content-Type: text/html; charset=utf-8\n\n')
print('''<HTML><BODY><H2>Page Web interactive Python</H2>
<FORM ACTION="http://127.0.0.1/brunotests/python/bonjour.py" METHOD="post">
<INPUT TYPE="submit" NAME="send" VALUE="Executer le script"></FORM>
</BODY></HTML>''')