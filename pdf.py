import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages
import os

# Chargement
employes = pd.read_csv("employes.csv")
absences = pd.read_excel("absences.xlsx")

# Préparation
employes["Date_Embauche"] = pd.to_datetime(employes["Date_Embauche"])
absences["Date"] = pd.to_datetime(absences["Date"])
employes["Anciennete"] = 2025 - employes["Date_Embauche"].dt.year

figures_dir = "figures"
os.makedirs(figures_dir, exist_ok=True)

# Histogramme de l'ancienneté
plt.figure(figsize=(7,4))
sns.histplot(employes["Anciennete"], bins=10)
plt.title("Ancienneté des employés")
plt.tight_layout()
plt.savefig(f"{figures_dir}/anciennete.png")
plt.close()

# Boxplot des salaires
plt.figure(figsize=(7,4))
sns.boxplot(data=employes, x="Service", y="Salaire")
plt.xticks(rotation=45)
plt.title("Salaires par service")
plt.tight_layout()
plt.savefig(f"{figures_dir}/salaires.png")
plt.close()