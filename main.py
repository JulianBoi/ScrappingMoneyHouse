# IMPORT

import json
import os


from lib.debug.debug import debug
from lib.properties.read_properties_file import read_properties_file
from lib.json.update_json_data import update_json_data
from lib.request.json_request import json_request
from lib.filter.multi_single_tab import multi_single_tab
from lib.request.data_request import data_request
from lib.csv.csv import convert_to_csv

# APPLICATION
def main():
    debug('DEBUG','Started ScrapHouse...')
    config = None
    try:
        config = read_properties_file('config/env-test.properties')
    except Exception:
        debug('WARN','La  configuration doit être reinitailisé !')


    started = int(config['configuration']['start'])
    ended = int(config['configuration']['end'])



    datas = []
    distant_json = []
    for i in range(started, ended):
        file = 'temp/page' + str(i) + '.json'
        if os.path.exists(file):
            with open(file, 'r') as file:
                distant_json = json.load(file)
            datas = distant_json['data']
        print("Récupération des données locale de la page :" + str(i))

    for i in range(started, ended):
        file = 'temp/page' + str(i) + '.json'
        if 'data' in datas:
            continue
            print("Donnée existante de la page : " + str(i) + "")
        print("Page " + str(i) + " créer")
        url = config['httprequest']['url'] + str(i)
        distant_json = json_request(url, {'Cookie': str(config['httprequest']['cookies']),
                                              'Cache-Control': str(config['httprequest']['cache'])
                                             }).json()['data']['results']
        print("Récupération des données de la page :" + str(i))
        update_json_data(file, {'data': distant_json})

    for data in distant_json:
        datas.append(data)

    data_add = {'data': []}
    file = 'temp/pages.json'

    print("Donnée de contact en cours de recupération")
    for data in datas:
        request = data_request(data['uri'],{'Cookie': str(config['httprequest']['cookies']),
        'Cache-Control': str(config['httprequest']['cache'])
        })
        if(request != None):
            if 'email' in request and 'phone' in request and 'site' in request:
                #TODO : Condition pour savoir ce que tu veux garder
                if request['email'] != "":
                    data_add['data'].append({
                                'id':data['id'],
                                'uri':data['uri'],
                                'currentName':data['currentName'],
                                'street':data['mainAddress']["street"],
                                'city':data['mainAddress']["city"],
                                'zip':data['mainAddress']["zip"],
                                'state':data['mainAddress']["state"],
                                'countryCode':data['mainAddress']["countryCode"],
                                'sectors':data['sectors'],
                                'purpose':data['purpose'],
                                'preferredLanguage':data['preferredLanguage'],
                                'capital':data['capital'],
                                'type':data['type'],
                                'employees':data['employees'],
                                'email':request['email'],
                                'site':request['site'],
                                'phone':request['phone'],
                            })

    print("Donnée mise dans le JSON")
    if os.path.exists(file):
        os.remove(file)
    update_json_data(file, data_add)

    convert_to_csv('temp/pages.json', 'csv/data.csv')

main()  