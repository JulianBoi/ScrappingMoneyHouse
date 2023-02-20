# IMPORT
import html


from lib.debug.debug import debug
from lib.properties.read_properties_file import read_properties_file
from lib.json.update_json_data import update_json_data
from lib.request.json_request import json_request
from lib.filter.multi_single_tab import multi_single_tab
from lib.request.data_request import data_request

# APPLICATION
def main():
    debug('DEBUG','Started ScrapHouse...')
    config = None
    try:
        config = read_properties_file('config/env-test.properties')
    except Exception:
        debug('WARN','La  configuration doit être reinitailisé !')

    datas = []
    started = int(config['configuration']['start'])
    ended = int(config['configuration']['end'])
    datas_fusion = []
    for i in range(started,ended):
        print("Page "+ str(i) +" créer")
        file = 'temp/page'+str(i)+'.json'
        data = update_json_data(file)
        if 'data' in data:
            continue
        url = config['httprequest']['url'] + str(i)
        distant_json = json_request(url,{'Cookie': str(config['httprequest']['cookies']),
        'Cache-Control': str(config['httprequest']['cache'])
        }).json()['data']['results']
        update_json_data(file,{'data':distant_json})
        datas.append(distant_json)
        print("Page "+ str(i) +" finalisé")
        file = 'temp/pages.json'
        datas_fusion = multi_single_tab(datas)
        data_add = {'data':[]}
    print("JSON en cours de création...")
    for data in datas_fusion:

        print("Search contact URI..."+ data['uri'])
        #Condition
        request = data_request(data['uri'],{'Cookie': str(config['httprequest']['cookies']),
        'Cache-Control': str(config['httprequest']['cache'])
        })
        if(request != None):
            if 'email' in request and 'phone' in request and 'site' in request:
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
        update_json_data(file,data_add)
    print("JSON créer")

main()  