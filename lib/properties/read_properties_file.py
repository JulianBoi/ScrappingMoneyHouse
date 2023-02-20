import configparser

def read_properties_file(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)
  
    config_map = {}
    for section in config.sections():
        config_map[section] = {}
        for key, value in config.items(section):
            config_map[section][key] = value
  
    return config_map

config_map = read_properties_file('config.properties')