import os
import requests
import csv
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/blacklist'

querystring = {
    'confidenceMinimum':'95',
    'limit':'20'
}

headers = {
    'Accept': 'application/json',
    'Key': '06e1f4327ddfe2598e013d9811d8afff122825bd131b58a3cf69f9839d6b6b67b7aace9626f83649'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# # Formatted output
# decodedResponse = json.loads(response.text) # class : dict

# json_object = json.dumps(decodedResponse, sort_keys=True, indent=4) # class : str 
decodedResponse = json.loads(response.text)

with open(os.path.join(os.getcwd(), ("blacklistedIPs_1.json")), "w") as file:
    json.dump(decodedResponse, file)

with open(os.path.join(os.getcwd(), ("blacklistedIPs_1.json")), "r") as file:
    loaded_json_data = json.load(file)

json_data = loaded_json_data['data']

csv_file = open(os.path.join(
    os.getcwd(), "blacklistedIPs_1.csv"), "w", newline="")
csv_writer = csv.writer(csv_file)

count = 0
for data in json_data:
    if count == 0:
        h = data.keys()
        csv_writer.writerow(h)
        count += 1
    csv_writer.writerow(data.values())

csv_file.close()

# current_dir = os.getcwd()

# json_obj = pd.read_json(response.text)
# json_obj.to_csv(os.path.join(current_dir,"blacklistedIPs.csv"))