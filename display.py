#pip install openpyxl matplotlib seaborn
#pip install -U ipykernel

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
#sns.histplot(employes["Anciennete"], bins=10, kde=False)
#plt.title("Ancienneté des employés")
#plt.xlabel("Années d'ancienneté")
#plt.ylabel("Nombre d'employés")
#plt.tight_layout()
#plt.show() #affichage via jupyter notebook
#plt.savefig("anciennete_employes.png")

#sns.boxplot(x="Service", y="Salaire", data=employes)
#plt.title("Distribution des salaires par service")
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.savefig("salaire_par_service.png")

#sns.countplot(x="Service", data=employes)
#plt.title("Effectifs par service")
#plt.ylabel("Effectifs")
#plt.tight_layout()
#plt.savefig("effectif_par_service.png")

absences["Mois"] = absences["Date"].dt.to_period("M").astype(str)
absences_mensuelles = absences.groupby("Mois")["Duree"].sum().cumsum()
#print(absences_mensuelles)
absences_mensuelles.plot(marker='o')
plt.title("Absences cumulées par mois")
plt.xlabel("Mois")
plt.ylabel("Durée cumulée des absences (jours)")
plt.tight_layout()
plt.savefig("absences_mensuelles.png")

merged = pd.merge(absences, employes[["ID", "Service"]], on="ID", how="left")
merged["Mois"] = merged["Date"].dt.to_period("M").astype(str)

pivot_table = merged.pivot_table(index="Service", columns="Mois", values="Duree", aggfunc="sum").fillna(0)

plt.figure(figsize=(10, 5))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="YlOrBr")
plt.title("Heatmap des absences par mois et service")
plt.tight_layout()
plt.savefig("absences_mos_services.png")



