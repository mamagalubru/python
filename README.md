# python
# mes essais et démonstrations python
# compte github : mamagalubru
# repository github : https://github.com/mamagalubru/python.git
# utiliser avec git


# récupérer une première fois un dossier github
# =============================================
# lancer git en local
# créer le dossier de réception locale (exemple : G:\github\mamagalubru\python)
# se positionner sur ce dossier
# effectuer un git clone du dépôt (exemple : git clone https://github.com/mamagalubru/python)

# pousser (push) une modification locale vers github
# ==================================================
# modifier le ou les fichierslancer
# lancer git en local
# se postionner sur répertoire local G:\github\mamagalubru\python
# vérifier le remote : 
	git remote -v 
	ou git remote show origin
	ou git config remote.origin.url
# git status (pour vérifier si des modifications ont été effectuées)
# git add fileschanged ou git commit -a (pour valider la modification locale)
# git push pour valider 

# récupérer (pull) une modification sur github vers le local
# ========================================
# tout repositionner comme ci-dessus
# git pull

