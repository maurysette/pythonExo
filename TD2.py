

def nouvelleFiche(vNom, vAge, vFonction, vTel, vMail, vAdresse):
    return {"nom": vNom, "age": vAge, "fonction": vFonction, "tel": vTel, "mail": vMail, "adresse": vAdresse}


def creationFiche(fiche):
    vNom = input("saisissez votre nom \n")
    vAge = int(input("saisissez votre age \n"))
    vFonction = input("saisissez votre fonction \n")
    vTel = int(input("saisissez votre téléphone \n"))
    vMail = input("saisissez votre mail \n")
    vAdresse = input("saisissez votre adresse \n")
    fiche1 = nouvelleFiche("qzdqz", 26, "qdzdzq",
                           24242424, "qddzqz", "qdqzqzdq")
    fiche = nouvelleFiche(vNom, vAge, vFonction, vTel, vMail, vAdresse)

    return (fiche)


def afficherPersonne(carnet):

    saisieUtilisateur = input("Veuillez saisir le nom pour la recherche \n")
    for index, valeurCarnet in enumerate(carnet):
        for i, valeurFiche in valeurCarnet.items():
            if valeurFiche == saisieUtilisateur:
                print(valeurCarnet.items())
            else:
                faux = False
                return (faux)
    if faux == False:
        print("Cet utilisateur n'a pas de fiche, veuillez la saisir !")


def afficherFiche(carnet):
    saisieUtilisateur = input(
        "Veuillez saisir le nom du champ pour la recherche \n")
    saisieUtilisateurValeur = input("veuillez saisir la valeur du champ \n")
    for index, valeurCarnet in enumerate(carnet):
        for i, valeurFiche in valeurCarnet.items():
            if valeurFiche == saisieUtilisateurValeur and i == saisieUtilisateur:
                print(valeurCarnet.items())
            else:
                faux = False
                return (faux)
    if faux == False:
        print("Les données sont innexactes !!")


def menu(carnet, fiche):
    for i in range(4):
        print("Veuillez choisir votre option \n"+"choix Q: sortir\n"+"choix C: saisir une fiche\n" +
              "choix A: chercher une personne \n" + "choix S: afficher une fiche")
        saisie = input()
        if saisie == 'C':
            fiche = creationFiche(fiche)
            print(fiche)
            carnet.append(fiche)
        elif saisie == 'A':
            afficherPersonne(carnet)
        elif saisie == 'S':
            afficherFiche(carnet)
        elif saisie == 'Q':
            break
        else:
            print("saisie incorrecte")


def main():
    carnet = []
    fiche = {}
    faux = True
    menu(carnet, fiche)


if __name__ == '__main__':
    main()
