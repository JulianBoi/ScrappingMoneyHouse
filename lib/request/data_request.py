import json
import requests
from bs4 import BeautifulSoup
import re

def data_request(value,headers):
    # faire une requête URL pour chaque valeur
    url = "https://www.moneyhouse.ch/fr/company/" + value
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    h4 = soup.find("h4", text="Coordonnées")

    email = ""
    site = ""
    phone = ""

    if h4:
        parent = h4.parent
        email = re.search(r'[\w\.-]+@[\w\.-]+', parent.text)
        if email:
            email = email.group(0)
        else:
            email = ""
        site = re.search(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', parent.text)
        if site:
            site = site.group(0)
        else:
            site = ""
        phone = re.search(r'\+\d{1,3}[- ]?\d{3,}[- ]?\d{3,}', parent.text)
        if phone:
            phone = phone.group(0)
        else:
            phone = ""
        coordinates_data = {"uri":value,"email": email, "site": site, "phone": phone}
        return coordinates_data
 
