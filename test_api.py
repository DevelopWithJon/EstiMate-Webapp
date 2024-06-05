# import requests
# import json
# from apps.api.routes import token_is_valid

# data = {'userId': 1, 'website': 'realtor.com', 'address': '435 main st', 'propertyId': 'M962534-93207', 'all_insurance': json.dumps([1,2,3]), 'all_water': json.dumps([1,2,4]), 'image': 'https://ap.rdcpix.com/a1e725a27180fcd2917cf5cb17c3fcb4l-m3991530636od-w480_h360_x2.webp'}

# r=requests.post("http://127.0.0.1:5000/api/report/a7af21c6784542e8a2cc4bdabe383433", data=(data))

# r = requests.get("http://127.0.0.1:5000/api/report/1")

# r = requests.get("http://127.0.0.1:5000/api/token/test/test")

import requests

url = "https://realtor.p.rapidapi.com/properties/list-sold"

querystring = {"state_code":"NY","city":"New York City","offset":"0","limit":"200","sort":"relevance","radius":"10"}

headers = {
	"X-RapidAPI-Key": "df37510f8emsh9b0b3cbe7382b61p1d66bbjsn7800b7ebe00b",
	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
