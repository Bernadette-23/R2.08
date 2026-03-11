import sys

def aide(msg_err):
    print(msg_err)
    print("usage : calc.py nombre operateur nombre")
    exit(1)

def test_io():
    if len(sys.argv) != 4:
        aide("Erreur : mauvais nombre d'arguments")

    try:
        nb1 = float(sys.argv[1])
        nb2 = float(sys.argv[3])
    except:
        aide("Erreur : nombres invalides")

    op = sys.argv[2]

    return nb1, op, nb2

def calculer(nb1, op, nb2):
    if op not in ["+", "-", "x", "/", "//", "%"]:
        aide("Opérateur invalide")

    if op == "+":
        return nb1 + nb2
    elif op == "-":
        return nb1 - nb2
    elif op == "x":
        return nb1 * nb2
    elif op == "/":
        return nb1 / nb2
    elif op == "//":
        return nb1 // nb2
    elif op == "%":
        return nb1 % nb2

# Programme principal
nb1, op, nb2 = test_io()
resultat = calculer(nb1, op, nb2)

print("Résultat :", resultat)'''