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