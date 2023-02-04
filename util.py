from datetime import datetime
import json
import re

def write_json_data(data, filename):
    with open(filename, 'w') as outfile:
                json.dump(data, outfile)

def string_to_num(str:str):
    return int(filter(str.isdigit, str))

# Strip longitude from Google Maps URI
def google_maps_url_to_longitude(google_maps_url:str):
    i = re.search("45.", google_maps_url).start()
    return google_maps_url[i:i+10]

# Strip latitude from Google Maps URI
def google_maps_url_to_latitude(google_maps_url:str):
    i = re.search("-75", google_maps_url).start()
    return google_maps_url[i:i+11]

def remove_duplicates_from_list(list:list):
    return [*set(list)]

# Get only phone number part from phone string. 
# Some phone numbers include extension, html elements or unnecessary words.
def get_phone_from_string(str:str):
    index = str.find("613")
    if index != -1:
        return str[index:index+12]
    else: return str