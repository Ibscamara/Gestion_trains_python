import csv
import math


def premiers_multiples(a: int, n: int) -> list[int]:
    if a < 2 or a > 100:
        raise ValueError("a doit être compris entre 2 et 100.")
    if n < 0 or n > 50:
        raise ValueError("n doit être compris entre 0 et 50.")

    multiples = []
    for i in range(1, n + 1):
        multiples.append(a * i)
    return multiples


def intersection_listes(x: list[int], y: list[int]) -> list[int]:
    resultat = []
    for element in x:
        if element in y and element not in resultat:
            resultat.append(element)
    return resultat


def moyenne_liste(liste: list[float]) -> float:
    if len(liste) == 0:
        raise ValueError("La liste ne doit pas être vide.")

    somme = 0
    for valeur in liste:
        somme += valeur
    return somme / len(liste)


def ecart_type(liste: list[float]) -> float:
    if len(liste) == 0:
        raise ValueError("La liste ne doit pas être vide.")

    moyenne = moyenne_liste(liste)
    somme_ecarts = 0
    for valeur in liste:
        somme_ecarts += (valeur - moyenne) ** 2

    variance = somme_ecarts / len(liste)
    return math.sqrt(variance)


def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("n doit être positif.")

    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat


def sont_multiples(a: int, b: int) -> bool:
    if a == 0 or b == 0:
        return False
    return a % b == 0 or b % a == 0


def lire_fichier_csv(nom_fichier: str) -> list[dict]:
    donnees = []
    with open(nom_fichier, mode="r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.DictReader(fichier, skipinitialspace=True)
        for ligne in lecteur:
            ligne["Nb_Passager"] = int(ligne["Nb_Passager"])
            donnees.append(ligne)
    return donnees


def ajouter_donnee_csv(
    nom_fichier: str,
    date: str,
    heure: str,
    numero_train: str,
    nombre_passagers: int,
) -> None:
    with open(nom_fichier, mode="a", encoding="utf-8", newline="") as fichier:
        champs = ["Date", "Heure", "Num_Train", "Nb_Passager"]
        ecrivain = csv.DictWriter(fichier, fieldnames=champs)

        ecrivain.writerow({
            "Date": date,
            "Heure": heure,
            "Num_Train": numero_train,
            "Nb_Passager": nombre_passagers,
        })
        

def extraire_nombres_passagers(donnees: list[dict]) -> list[int]:
    resultats = []
    for ligne in donnees:
        resultats.append(int(ligne["Nb_Passager"]))
    return resultats


def minimum_passagers(donnees: list[dict]) -> int:
    nombres = extraire_nombres_passagers(donnees)
    if len(nombres) == 0:
        raise ValueError("Aucune donnée disponible.")

    minimum = nombres[0]
    for valeur in nombres:
        if valeur < minimum:
            minimum = valeur
    return minimum


def maximum_passagers(donnees: list[dict]) -> int:
    nombres = extraire_nombres_passagers(donnees)
    if len(nombres) == 0:
        raise ValueError("Aucune donnée disponible.")

    maximum = nombres[0]
    for valeur in nombres:
        if valeur > maximum:
            maximum = valeur
    return maximum


def moyenne_passagers(donnees: list[dict]) -> float:
    nombres = extraire_nombres_passagers(donnees)
    return moyenne_liste(nombres)