# Fonctions
def calculer_anciennete(annee_embauche, annee_fin):
    resultat = annee_fin - annee_embauche
    return resultat


# Déclaration variables

prenom = "Alice"
age = 30
salaire = 2500.75
actif = True
# Affichage des variables
print(prenom, age)

# opérations simples
heure_par_semaine = 35
taux_horaire = salaire / heure_par_semaine
print("Taux horaire : ", round(taux_horaire, 2))

# conditions
if age > 45:
    print("Employé senior")
else:
    print("Employé junior")

# itérations
services = ["Développement", "Marketing", "Ventes"]
print(services)
for service in services:
    print("Service :", service)

index = 0
while index < len(services):
    print("Service :", services[index])
    index += 1 # index = index + 1

# matrices
matrice = [
    [5, 10, 15],
    [8, 18, 2],
    [7, 8, 9]
]
print(matrice[1][1])

# listes
services.append("Support")
services.insert(1, "R&D")
services.remove("Ventes")
print(services)

# dictionnaires
salaire_par_employe = {"Alice": 2500.75, "Bob": 3000.50, "Charlie": 2800.00}
print(salaire_par_employe["Bob"])



anciennete = calculer_anciennete(2015, 2023)
print("Ancienneté :", anciennete, "ans")


