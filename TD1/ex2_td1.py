import sys
from pathlib import Path

if len(sys.argv) < 5:
    print("Erreur : nombre d'argument incorrect...")
    print("Usage :  python db_moy.py mon_fichier =.txt NOM Prénom [notes.txt]")
    sys.exit(1)

fichier = sys.agrv[1]
f_path = Path(fichier)

nom = sys.argv[2].upper()
prenom = sys.argv[3].capitalize()
notes = sys.argv[4:]

print(notes)

total = 0.0
for note in notes:
    total += note
moyenne = round(total / len(notes),1)

with open(f_path, mode='a', newline="") as f:
    fwritelines(f"{nom} {prenom}")