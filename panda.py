import pandas as pd
import math

# charger les données
data_file = pd.read_csv('employes.csv')

#print(data_file.head())

# infos sur le data frame
#print(data_file.info())
#print(data_file.describe())

#print(data_file[["Nom","Salaire"]])

# employés du service RH
print(data_file[data_file["Service"] == "RH"])

# employés avec salaire sup à 2600€
#print(data_file[[data_file["Salaire"] > 2600]])

# Nom et Salaire employés avec salaire sup à 2600€
print(data_file.loc[data_file["Salaire"] > 2600][["Nom", "Salaire","Service"]])

data_file.fillna(0, inplace=True)  # Remplacer les valeurs manquantes par 0

#data_file["Salaire"] = data_file["Salaire"].fillna(0)#data_file["Salaire"].me"Salairean())

# Tri par salaires
print(data_file.sort_values("Salaire", ascending=False))

data_file["Anciennete"] = 2025 - pd.to_datetime(data_file["Date_Embauche"]).dt.year  # Calcul de l'ancienneté en années
print(data_file)

# salaire moyen par service
print(data_file.groupby("Service")["Salaire"].mean().apply(math.floor))
