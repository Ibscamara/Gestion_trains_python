class Etudiant:
    def __init__(self, nom: str, prenom: str, date_naissance: str, numero_etudiant: str):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.numero_etudiant = numero_etudiant

    def afficher_infos(self) -> str:
        return (
            f"Nom : {self.nom}\n"
            f"Prénom : {self.prenom}\n"
            f"Date de naissance : {self.date_naissance}\n"
            f"Numéro étudiant : {self.numero_etudiant}"
        )


class Formation:
    def __init__(self, intitule: str, specialite: str):
        self.intitule = intitule
        self.specialite = specialite
        self.etudiants = []

    def ajouter_etudiant(self, etudiant: Etudiant) -> None:
        self.etudiants.append(etudiant)

    def afficher_formation(self) -> str:
        texte = f"Formation : {self.intitule}\nSpécialité : {self.specialite}\n"
        texte += "Liste des étudiants :\n"

        for etudiant in self.etudiants:
            texte += f"- {etudiant.prenom} {etudiant.nom} ({etudiant.numero_etudiant})\n"

        return texte