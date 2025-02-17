import requests
import json

id = 3608
city = "Registro"
stateAbbreviation = "SP"
countryAbbreviation = "BR"
days = 15

TOKEN = "1a4e63a42bb2c896315e86930374ee33"
BASEURL = "http://apiadvisor.climatempo.com.br/api/v1/"

URLFORECAST = BASEURL + "/forecast/locale/" + str(id) + "/days/" + str(days) + "?token=" + TOKEN 

response = requests.get(BASEURL)


if response.status_code == 200:
    obj = response.json()
    
    print(obj)
    