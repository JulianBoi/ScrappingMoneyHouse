import os
import json

def update_json_data(filename, data_to_add = {}):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(data_to_add, f,indent=4)
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        data.update(data_to_add)
        with open(filename, 'w') as f:
            json.dump(data, f,indent=4)
        return data
    except json.JSONDecodeError:
        os.remove(filename)
        data = {}
        data.update(data_to_add)
        with open(filename, 'w') as f:
            json.dump(data, f,indent=4)
        return data

