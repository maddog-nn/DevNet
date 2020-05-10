import requests

url = "https://lgb-netbox01.int/api/dcim/interfaces?device=mia-wvrtcore-a"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Token NetBox Token'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
print('test from windows!')