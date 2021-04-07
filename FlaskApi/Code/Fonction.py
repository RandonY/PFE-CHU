import json

with open("data.json", "r") as read_file:
    fake_data = json.load(read_file)

def parse_info_to_list(type):
    info_data = []
    value_data = []
    date_info = fake_data.keys()
    for date in date_info:
        value_data.append(date)
        if type in ["polluants","meteo","hopital"]:
            for word in fake_data.get(date).get(type):
                value_data.append(fake_data.get(date).get(type).get(word))
            info_data.append(value_data)
            value_data = []
    return info_data
