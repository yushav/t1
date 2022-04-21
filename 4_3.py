#4_3
import requests
import json
import datetime


def currency_rates( val):
  url = 'https://www.cbr-xml-daily.ru/daily_json.js'
  val = val.upper()

  response = requests.get(url)
  dict_val = json.loads(response.text)
  dt = dict_val['Date']
  
 #print(type(dict_val['Valute']['USD']['Value']))
  if val in dict_val['Valute']:
    return dict_val['Valute'][val]['Value'], dt
  return None


print('EUR :', *currency_rates('EUR'))
print('USD :', *currency_rates('usd'))