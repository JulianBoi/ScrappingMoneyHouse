import json
import csv
from lib.properties.read_properties_file import read_properties_file

def convert_to_csv(json_file, csv_file):
    properties = read_properties_file('config/params.properties')
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        # Write the header row
        writer.writerow(['id', 'uri','nameDirector', 'currentName','street','city','zip','state','countryCode','sectors','purpose','preferredLanguage','capital','type','employees','email','site','phone'])

        # Write the data rows
        for data in json_data['entreprises']:
            if properties['params']['demand'] in data:
                if properties['params']['demand'] != "":
                    if data[properties['params']['demand']] != "":
                        writer.writerow(
                            [data['id'],
                            data['uri'],
                            data['nameDirector'],
                            data['currentName'],
                            data["street"],
                            data["city"],
                            data["zip"],
                            data["state"],
                            data["countryCode"],
                            data['sectors'],
                            data['purpose'],
                            data['preferredLanguage'],
                            data['capital'],
                            data['type'],
                            data['employees'],
                            data['email'],
                            data['site'],
                            data['phone']])
                else :
                    writer.writerow(
                        [data['id'],
                         data['uri'],
                         data['nameDirector'],
                         data['currentName'],
                         data["street"],
                         data["city"],
                         data["zip"],
                         data["state"],
                         data["countryCode"],
                         data['sectors'],
                         data['purpose'],
                         data['preferredLanguage'],
                         data['capital'],
                         data['type'],
                         data['employees'],
                         data['email'],
                         data['site'],
                         data['phone']])
