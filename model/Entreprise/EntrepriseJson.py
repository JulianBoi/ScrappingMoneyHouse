# -*- coding: utf-8 -*-
import json

class EntrepriseJson:
    def __init__(self, filename):
        self.filename = filename
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.entreprises = json.load(f)
        except Exception as e:
            print('JSON  reinitialisé')
            with open('temp/entreprise.json', 'w') as f:
                json.dump({"entreprises": []}, f, indent=4)
                exit()

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.entreprises, f, indent=4)

    def add_entreprise(self, entreprise):
        self.entreprises['entreprises'].append(entreprise)
        self.save()

    def update_entreprise(self, id, new_entreprise):
        for i in range(len(self.entreprises)):
            if self.entreprises['entreprises'][i]['id'] == id:
                self.entreprises['entreprises'][i] = new_entreprise
                self.save()
                return True
        return False

    def delete_entreprise(self, id):
        for i in range(len(self.entreprises)):
            if self.entreprises['entreprises'][i]['id'] == id:
                del self.entreprises['entreprises'][i]
                self.save()
                return True
        return False
