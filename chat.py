

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