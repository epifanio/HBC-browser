import yaml

def get_settings():
    settings = open("config/config.yaml", 'r')
    dictionary = yaml.load(settings)
    return dictionary
