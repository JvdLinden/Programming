import requests
import xmltodict
auth_detail = ('joren.vanderlinden@student.hu.nl', 'DBdJv2sVyFiZVWJoFJ0A9rig8TCwzUPku_MmU3_FZK3G7sYZHtJ3IQ')
api_url = ('http://webservices.ns.nl/ns-api-avt?station=ut')

response = requests.get(api_url, auth=auth_detail)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']
    vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16] # 18:36
    print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)
