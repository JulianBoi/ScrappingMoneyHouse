# -*- coding: utf-8 -*-
    #
    # Cette classe représente une entreprise et ses attributs associés.
    #
    # Attributs:
    # ----------
    # id : int
    #     Identifiant de l'entreprise.
    # uri : str
    #     URI de l'entreprise.
    # nameDirector : str
    #     Nom du directeur de l'entreprise.
    # coordDirectors : str
    #     Coordonnées du directeur de l'entreprise.
    # currentName : str
    #     Nom actuel de l'entreprise.
    # street : str
    #     Rue de l'adresse de l'entreprise.
    # city : str
    #     Ville de l'adresse de l'entreprise.
    # zip : str
    #     Code postal de l'adresse de l'entreprise.
    # state : str
    #     État de l'adresse de l'entreprise.
    # countryCode : str
    #     Code de pays de l'adresse de l'entreprise.
    # sectors : str
    #     Secteurs d'activité de l'entreprise.
    # purpose : str
    #     Objectif de l'entreprise.
    # preferredLanguage : str
    #     Langue préférée de l'entreprise.
    # capital : float
    #     Capital de l'entreprise.
    # type : str
    #     Type d'entreprise.
    # employees : int
    #     Nombre d'employés de l'entreprise.
    # email : str
    #     Adresse email de l'entreprise.
    # site : str
    #     Site web de l'entreprise.
    # phone : str
    #     Numéro de téléphone de l'entreprise.
    #
class Entreprise:
    def __init__(self, uri, nameDirector, coordDirectors, currentName, street, city, zip, state, countryCode, sectors, purpose, preferredLanguage, capital, type, employees, email, site, phone,archive):
        self.id = None
        self.uri = uri
        self.nameDirector = nameDirector
        self.coordDirectors = coordDirectors
        self.currentName = currentName
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.countryCode = countryCode
        self.sectors = sectors
        self.purpose = purpose
        self.preferredLanguage = preferredLanguage
        self.capital = capital
        self.type = type
        self.employees = employees
        self.email = email
        self.site = site
        self.phone = phone
        self.archive = archive