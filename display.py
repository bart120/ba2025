import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
employes = pd.read_csv("employes.csv")
absences = pd.read_excel("absences.xlsx")

# Préparation
employes["Date_Embauche"] = pd.to_datetime(employes["Date_Embauche"])
absences["Date"] = pd.to_datetime(absences["Date"])
employes["Anciennete"] = 2025 - employes["Date_Embauche"].dt.year




plt.figure(figsize=(8, 5))
sns.histplot(employes["Anciennete"], bins=10, kde=False)
plt.title("Répartition de l'ancienneté des employés")
plt.xlabel("Ancienneté (années)")
plt.ylabel("Nombre d'employés")
plt.tight_layout()
#plt.show()
plt.savefig("anciennete_histogramme.png")