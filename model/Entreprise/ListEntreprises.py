# -*- coding: utf-8 -*-
import json

class ListEntreprises:
    # initialisation de la liste d'entreprises
    def __init__(self):
        self.entreprises = []
        self.next_id = 1

    # ajout d'une entreprise à la liste et mise à jour de l'ID
    def add(self, entreprise):
        entreprise.id = self.next_id
        self.entreprises.append(entreprise)
        self.next_id += 1

    # mise à jour d'une entreprise dans la liste
    def update(self, id_entreprise, nouvelle_entreprise):
        for entreprise in self.entreprises:
            if entreprise.id == id_entreprise:
                nouvelle_entreprise.id = id_entreprise
                self.entreprises[self.entreprises.index(entreprise)] = nouvelle_entreprise
                return True
        return False

    # suppression d'une entreprise dans la liste
    def delete(self, id_entreprise):
        for entreprise in self.entreprises:
            if entreprise.id == id_entreprise:
                self.entreprises.remove(entreprise)
                return True
        return False

    # récupération de la liste d'entreprises
    def get_all(self):
        entreprises_json = []
        for entreprise in self.entreprises:
            entreprise_dict = entreprise.__dict__
            entreprises_json.append(entreprise_dict)
        return data.dumps({"entreprises": entreprises_json})

    # récupération d'une entreprise par son ID
    def get_by_id(self, id_entreprise):
        for entreprise in self.entreprises:
            if entreprise.id == id_entreprise:
                entreprise_dict = entreprise.__dict__
                return entreprise_dict
        return None