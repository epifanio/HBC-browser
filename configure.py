import yaml


def get_settings():
    settings = open("config/config.yaml", 'r')
    dictionary = yaml.load(settings)
    return dictionary



def validate_settings():
    settings = get_settings()
    # TODO 
    # check for existing directory
    # hbcbrowser -> imagepath <-- check if has images
    # export -> kmldir
    # export -> vrtdir
    # check for existing files
    # hbcbrowser -> imagemetadata
    # file browser
    # filemanager
    # WMS basemap
    # mapviewer -> basemap
    return settings