from fonctions import (
    premiers_multiples,
    intersection_listes,
    moyenne_liste,
    ecart_type,
    factorielle,
    sont_multiples,
    lire_fichier_csv,
    ajouter_donnee_csv,
    moyenne_passagers,
    minimum_passagers,
    maximum_passagers,
)
from classe import Etudiant, Formation


def tester_fonctions_de_base() -> None:
    print("=== TEST DES FONCTIONS DE BASE ===")

    print("10 premiers multiples de 3 :")
    print(premiers_multiples(3, 10))

    x1 = [40, 21, 8, 19, -6, 27, 45]
    y1 = [39, 21, 8, 20, 44]
    print("\nIntersection de deux listes :")
    print(intersection_listes(x1, y1))

    liste_nombres = [12, 15, 18, 20, 10]
    print("\nMoyenne de la liste :")
    print(moyenne_liste(liste_nombres))

    print("\nÉcart-type de la liste :")
    print(round(ecart_type(liste_nombres), 2))

    print("\nFactorielle de 5 :")
    print(factorielle(5))

    print("\n12 et 3 sont-ils multiples l'un de l'autre ?")
    print(sont_multiples(12, 3))


def tester_csv() -> None:
    print("\n=== TEST DE LA GESTION CSV ===")

    nom_fichier = "passager-train.csv"

    donnees = lire_fichier_csv(nom_fichier)
    print("\nDonnées initiales :")
    for ligne in donnees:
        print(ligne)

    # Ajout d'une donnée de test
    #ajouter_donnee_csv(nom_fichier, "15-12-2025", "15h07", "TER245", 132)
import re
from datetime import datetime

def ajouter_train_interactif() -> None:
    print("\n=== AJOUT D'UN TRAIN ===")

    nom_fichier = "passager-train.csv"

    # Vérification de la date
    while True:
        date = input("Entrez la date (ex: 15-12-2025) :  ")
        try:
            datetime.strptime(date, " %d-%m-%Y")
            break
        except ValueError:
            print("Format de date invalide. Utilisez jj-mm-aaaa.")

    # Vérification de l'heure
    while True:
        heure = input("Entrez l'heure (ex: 15h07) : ")
        try:
            datetime.strptime(heure, "%Hh%M")
            break
        except ValueError:
            print("Format d'heure invalide. Utilisez hhHMM (ex: 15h07).")

    numero_train = input("Entrez le numéro du train (ex:TER123 ) :  ")
    
    # Vérification du numéro du train
    while True:
        numero_train = input("Entrez le numéro du train (ex: TER245) : ")
        if re.match(r"^[A-Za-z_]+[0-9]+$", numero_train):
            break
        else:
            print("Numéro de train invalide. Exemple : TER245 ou Train_001")


    # Vérification du nombre de passagers
    while True:
        try:
            nombre_passagers = int(input("Entrez le nombre de passagers : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    ajouter_donnee_csv(nom_fichier, date, heure, numero_train, nombre_passagers)

    print("Train ajouté avec succès !")

    donnees = lire_fichier_csv(nom_fichier)
    print("\nDonnées après ajout :")
    for ligne in donnees:
        print(ligne)

    print("\nStatistiques sur les passagers :")
    print("Moyenne :", round(moyenne_passagers(donnees), 2))
    print("Minimum :", minimum_passagers(donnees))
    print("Maximum :", maximum_passagers(donnees))


def tester_classes() -> None:
    print("\n=== TEST DES CLASSES ===")

    etudiant1 = Etudiant("Camara", "Ibrahima Sory", "28/06/1999", "20223545")
    etudiant2 = Etudiant("Diallo", "Mamadou", "15/03/2000", "20224567")
    etudiant3 = Etudiant("Barry", "Aissatou", "02/09/2001", "20225678")

    print("\nInformations d'un étudiant :")
    print(etudiant1.afficher_infos())

    formation = Formation("Licence Mathématiques", "Statistique et analyse de données")
    formation.ajouter_etudiant(etudiant1)
    formation.ajouter_etudiant(etudiant2)
    formation.ajouter_etudiant(etudiant3)

    print("\nInformations sur la formation :")
    print(formation.afficher_formation())


def main() -> None:
    tester_fonctions_de_base()
    tester_csv()
    ajouter_train_interactif()
    tester_classes()


if __name__ == "__main__":
    main()
    