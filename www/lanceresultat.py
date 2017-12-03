#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

# on lance le programme résultat en remplissant puis en cliquant

print('Content-Type: text/html; charset=utf-8\n\n')
print('''<HTML><BODY>
<H3>Page web produite par un script Python</H3>
<FORM ACTION="resultat.py" METHOD="post">
<P>Veuillez entrer votre nom dans le champ ci-dessous, s.v.p. :</P>
<P><INPUT NAME="visiteur" SIZE=20 MAXLENGTH=20 TYPE="text"></P>
<P>Veuillez également me fournir une phrase quelconque :</P>
<TEXTAREA NAME="phrase" ROWS=2 COLS=50>Mississippi</TEXTAREA>
<P>J'utiliserai cette phrase pour établir un histogramme.</P>
<INPUT TYPE="submit" NAME="send" VALUE="Action">
</FORM></BODY></HTML>''')
