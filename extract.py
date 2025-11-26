import re

# --- chemins exacts de vos fichiers ---
FICHIER_TEXT   = r'/home/cerine/Documents/EI/Extraction/80_jours.txt'
FICHIER_DICO   = r'/home/cerine/Documents/EI/Extraction/Person.dic'
FICHIER_RESULT = r'/home/cerine/Documents/EI/Extraction/result_UTF8BOM.txt'

# 1) charge les noms complets (Prénom Nom) du dictionnaire
noms = set()
with open(FICHIER_DICO, 'r', encoding='utf-16-le') as f:
    for ln in f:
        forme = ln.split(',', 1)[0].strip()
        if forme.count(' ') == 1:
            noms.add(forme.lower())
print(f'→ {len(noms)} formes chargées depuis {FICHIER_DICO}')

# 2) extraction sans répétition
trouves = set()
with open(FICHIER_TEXT, 'r', encoding='utf-16-le') as src:
    txt = src.read()
    for pren, nom in re.findall(r'\b([A-Z]\w*)\s+([A-Z]\w*)\b', txt):
        ligne = f'{pren} {nom}'
        if ligne.lower() in noms:
            trouves.add(ligne)

# 3) écriture + affichage (triés, sans doublon)
with open(FICHIER_RESULT, 'w', encoding='utf-8-sig') as out:
    for ligne in sorted(trouves):
        out.write(f'Resultat : {ligne}\n')
        print(f'Resultat : {ligne}')

print('Extraction was a success!')