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

# rapport PDF

#pdf = PdfPages(f"{figures_dir}/rapports.pdf")
#....
#pdf.close() # 2 lignes remplacées par le "with"
with PdfPages(f"{figures_dir}/rapports.pdf") as pdf:
    for file in os.listdir(figures_dir):
        if file.endswith(".png"):
            fig = plt.figure()
            img = plt.imread(f"{figures_dir}/{file}")
            plt.imshow(img)
            plt.axis("off")
            pdf.savefig(fig)
            plt.close()

# rapport excel
with pd.ExcelWriter("rapport_rh.xlsx") as writer:
    employes.to_excel(writer, sheet_name="Employes", index=False)
    absences.to_excel(writer, sheet_name="Absences", index=False)

    taux = absences.groupby("ID")["Duree"].sum().reset_index()
    merged = pd.merge(employes, taux, on="ID", how="left").fillna(0)
    merged["Taux"] = merged["Duree"] / merged["Anciennete"]

    #merged[["ID", "Nom", "Service", "Anciennete", "Taux"]].to_excel(writer, sheet_name="Taux_absence", index=False)
    merged[["ID", "Nom", "Service", "Anciennete", "Duree"]].to_excel(writer, sheet_name="Taux_absence", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Taux_absence"]

    worksheet.write(0, 5, "Taux")
    for row in range(1, len(merged)+1):
        formule = f"=IF(D{row+1}=0, 0, E{row+1}/D{row+1})"
        worksheet.write(row, 5, formule)





