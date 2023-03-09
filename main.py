# -*- coding: utf-8 -*-
import re
from builtins import PermissionError

from bs4 import BeautifulSoup

from model.Entreprise.EntrepriseJson import EntrepriseJson
from model.Entreprise.ListEntreprises import ListEntreprises
from model.Entreprise.Entreprise import Entreprise
from lib.properties.read_properties_file import read_properties_file
from lib.csv.csv import convert_to_csv

import requests
import json
import csv
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



# 1- CONFIGURATION


# 2 - PARAMS
properties = read_properties_file('config/params.properties')


params={}

pageMAX = properties['params']['page']

if properties['params']['limit'] != "":
    params['limit']= properties['params']['limit']
if properties['params']['status'] != "":
    params['status']= properties['params']['status']
if properties['params']['legal'] != "":
    params['legalForm']= str(properties['params']['legal'])
if properties['params']['turnover'] != "":
    params['turnoverRanges']= str(properties['params']['turnover'])
if properties['params']['employee'] != "":
    params['employeeRanges']= str(properties['params']['employee'])
if properties['params']['participations'] != "":
    params['hasParticipations']= str(properties['params']['participations'])
if properties['params']['brands'] != "":
    params['hasBrands']= str(properties['params']['brands'])
if properties['params']['building'] != "":
    params['hasBuildingProjects']= str(properties['params']['building'])
if properties['params']['jobs'] != "":
    params['hasJobs']= str(properties['params']['jobs'])
if properties['params']['country'] != "":
    params['country']= str(properties['params']['country'])
if properties['params']['sector'] != "":
    params['sector']= str(properties['params']['sector'])
if properties['params']['zip'] != "":
    params['zipCodes']= str(properties['params']['zip'])
if properties['params']['domicile'] != "":
    params['domicile']=str(properties['params']['domicile'] )
if properties['params']['history']  != "":
    params['withHistory']=str(properties['params']['history'])
if properties['params']['offset'] != "":
    params['offset']=properties['params']['offset']
if properties['params']['name'] != "":
    params['name']=properties['params']['name']





try:
    json_file = EntrepriseJson("temp/entreprise.json")
except Exception as e:
    print('JSON  reinitialisé')
    with open('temp/entreprise.json', 'w') as f:
        json.dump({"entreprises": []}, f, indent=4)
        exit()

uriJSONLocal = []

# 2.3.2 - LIST DATA DISTANTE
listEntrepriseDistant = ListEntreprises()

for data in json_file.entreprises["entreprises"]:
    uriJSONLocal.append(data["uri"])
    entrepriseLocal = Entreprise(
        #  URI de l'entreprise.
        data["uri"],
        # Nom du directeur de l'entreprise.
        data["nameDirector"],
        #  Coordonnées du directeur de l'entreprise.
        data["coordDirectors"],
        #  Nom actuel de l'entreprise.
        data["currentName"],
        # Rue de l'adresse de l'entreprise.
        data["street"],
        # Ville de l'adresse de l'entreprise.
        data["city"],
        # Code postal de l'adresse de l'entreprise.
        data["zip"],
        # État de l'adresse de l'entreprise.
        data["state"],
        # Code de pays de l'adresse de l'entreprise.
        data["countryCode"],
        # Secteurs d'activité de l'entreprise.
        data["sectors"],
        # Objectif de l'entreprise.
        data["purpose"],
        # Langue préférée de l'entreprise.
        data["preferredLanguage"],
        # Capital de l'entreprise.
        data["capital"],
        # Type d'entreprise.
        data["type"],
        # Nombre d'employés de l'entreprise.
        data["employees"],
        # Adresse email de l'entreprise.
        data["email"],
        # Site web de l'entreprise.
        data["site"],
        # Numéro de téléphone de l'entreprise.
        data["phone"],
        # Ancien ou non ?
        True)
    listEntrepriseDistant.add(entrepriseLocal)





# 2 - BOUCLE SUR CHAQUE PAGE
for page in range(0,int(pageMAX)):
    if page != "":
        params['page'] = str(page)
    # 2.1 - URL CREATED
    url = "https://www.moneyhouse.ch/fr/jx/advanced-search-results-partial"

    # 2.2 - DATA DISTANTE
    response = requests.get(url, headers={
        # TODO:     COOKIES
    }, params=params)

    # 2.3 - VERIFIER SI ON RECUPERE BIEN DES DONNEES
    if response.status_code == 200 or response.status_code == 304:
        print('Traitement du lien :' + str(response.url))
        # 2.3.1 - METTRE LE JSON EN PLACE
        json_data = response.json()

        #2.3.3 - CREER LES ENTREPRISES ET LE INSERER DANS LA LISTE
        for data in json_data["data"]["results"]:
            if data != None :
                uriValidator = True
                for uriJSON in uriJSONLocal:
                    if uriJSON == data['uri']:
                        uriValidator = False
                if uriValidator:
                    # 2.3.3.1 - DONNER ENVOYER
                    entrepriseDistante = Entreprise(
                        #  URI de l'entreprise.
                        data["uri"],
                        # Nom du directeur de l'entreprise.
                        "",
                        #  Coordonnées du directeur de l'entreprise.
                        data["contactDetails"] if "contactDetails" in data else "",
                        #  Nom actuel de l'entreprise.
                        data["currentName"] if "currentName" in data else "",
                        # Rue de l'adresse de l'entreprise.
                        data["mainAddress"]["street"] if "mainAddress" in data and "street" in data['mainAddress'] else "",
                        # Ville de l'adresse de l'entreprise.
                        data["mainAddress"]["city"] if "mainAddress" in data and "city" in data['mainAddress'] else "",
                        # Code postal de l'adresse de l'entreprise.
                        data["mainAddress"]["zip"] if "mainAddress" in data and "zip" in data['mainAddress'] else "",
                        # État de l'adresse de l'entreprise.
                        data["mainAddress"]["state"] if "mainAddress" in data and "state" in data['mainAddress'] else "",
                        # Code de pays de l'adresse de l'entreprise.
                        data["mainAddress"]["countryCode"] if "mainAddress" in data and "countryCode" in data['mainAddress'] else "",
                        # Secteurs d'activité de l'entreprise.
                        data["sectors"] if "sectors" in data else "",
                        # Objectif de l'entreprise.
                        data["purpose"] if "purpose" in data else "",
                        # Langue préférée de l'entreprise.
                        data["preferredLanguage"] if "preferredLanguage" in data else "",
                        # Capital de l'entreprise.
                        data["capital"] if "capital" in data else "",
                        # Type d'entreprise.
                        data["type"] if "type" in data else "",
                        # Nombre d'employés de l'entreprise.
                        data["employees"] if "employees" in data else "",
                        # Adresse email de l'entreprise.
                        "",
                        # Site web de l'entreprise.
                        "",
                        # Numéro de téléphone de l'entreprise.
                        "",
                        # Ancien ou non ?
                        False)
                    # 2.3.3.2 - COORDONNER RECUPERER
                    urlCoord = "https://www.moneyhouse.ch/fr/company/" + str(data['uri'])
                    response = requests.get(urlCoord,headers={
                    # TODO:     COOKIES
                    })
                    # 2.3.3.3 - Parcours de la page


                    soup1 = BeautifulSoup(response.content, "html.parser")

                    h4 = soup1.find("h4", text="Coordonnées")

                    if h4:
                        parent = h4.parent
                        email = re.search(r'[\w\.-]+@[\w\.-]+', parent.text)
                        if email:
                            entrepriseDistante.email = email.group(0)
                        else:
                            entrepriseDistante.email = ""
                        site = re.search(
                            r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})',
                            parent.text)
                        if site:
                            entrepriseDistante.site = site.group(0)
                        else:
                            entrepriseDistante.site = ""
                        phone = re.search(r'\+\d{1,3}[- ]?\d{3,}[- ]?\d{3,}', parent.text)
                        if phone:
                            entrepriseDistante.phone = phone.group(0)
                        else:
                            entrepriseDistante.phone = ""
                    soup = BeautifulSoup(response.content, "html.parser")
                    h4bis= soup.find("h4", text="Organe de gestion")

                    if h4bis:
                        parent = h4bis.parent.text.replace('Organe de gestion', '', 1).strip()
                        if parent:
                            entrepriseDistante.nameDirector = parent
                        else:
                            entrepriseDistante.nameDirector = ""
                    listEntrepriseDistant.add(entrepriseDistante)
                    json_file.add_entreprise(listEntrepriseDistant.get_by_id(entrepriseDistante.id))


    else:
        print("[Code HTTP ERROR] : " + str(response.status_code) + " => erreur de params ou serveur INACTIF : tester ce lien "+str(response.url))
try:
    convert_to_csv('temp/entreprise.json', 'file/export.csv')
except PermissionError:
    print('CSV Non-Fermé !')
