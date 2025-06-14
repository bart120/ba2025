OPEN_API_KEY = ""

#pip install openai dotenv

#pip uninstall openai
#pip install openai==0.28

import openai
import pandas as pd
import os


def generer_reco(nom, poste, anciennete):
    prompt = f"""
    En tant que consultant RH, propose une recommandation de développement professionnel pour un employé nommé {nom},
    travaillant comme {poste} depuis {anciennete} années. Donne des suggestions précises en une phrase. PRopose moi pluseiurs choix, 3 au minimum dont un à l'internationnal.
    """

    reponse = openai.ChatCompletion.create(
        model = "gpt-4.1",
        messages = [{"role": "user", "content" : prompt}],
        temperature = 0.7
    )    
    #print(reponse)
    return reponse["choices"][0]["message"]["content"].strip()


openai.api_key = OPEN_API_KEY

# charger les données RH
data = pd.read_csv("employes.csv")

reco = generer_reco("Wassila", "consultante en relation des employés", 5)
print(reco)

def generer_rapport(df):
    nb = len(df)
    df["Age"] = 2025 - pd.to_datetime(df["Date_Naissance"]).dt.year
    moyenne_age = df['Age'].mean()
    nb_femmes = df[df['Sexe'] == 'F'].shape[0]
    prompt = f"""
    Rédige un rapport synthétique RH destiné à la direction, basé sur les éléments suivants :
    - Nombre total d'employés : {nb}
    - Âge moyen : {moyenne_age:.1f}
    - Nombre de femmes : {nb_femmes}
    Présente cela de façon claire et concise.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response["choices"][0]["message"]["content"].strip()
print(generer_rapport(data))