import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("--> usage : extract_log.py nom_fichier.log mot_cle")
    exit(1)

f_path = Path(sys.argv[1]).resolve()
mot_cle = sys.argv[2]

if not f_path.exists():
    print("Erreur : le fichier n'existe pas.")
    exit(1)

if not f_path.is_file():
    print("Erreur : le chemin indiqué n'est pas un fichier.")
    exit(1)

if mot_cle not in ["ERROR", "WARNING", "INFO"]:
    print("Erreur : le mot clé doit être ERROR, WARNING ou INFO.")
    exit(1)

compteur = 0

with open(f_path, mode="r", encoding="utf-8") as file:
    for ligne in file:
        if mot_cle in ligne:
            compteur += 1

print(f"Le nombre de lignes contenant {mot_cle} est : {compteur}")