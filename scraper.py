import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fr.wikipedia.org/wiki/Liste_des_langages_de_programmation"
response = requests.get(url)
if response.status_code != 200:
    print("Erreur lors du chargement de la page")
    exit()

soup = BeautifulSoup(response.text, "lxml")
divs = soup.find_all("div", class_="div-col")

langages = []
for div in divs:
    for li in div.find_all("li"):
        nom = li.text.strip()
        if nom and nom not in langages:
            langages.append(nom)

df = pd.DataFrame(langages, columns=["Langage"])
df.to_csv("data.csv", index=False, encoding="utf-8")

print("Fichier 'data.csv' généré avec", len(df), "langages.")