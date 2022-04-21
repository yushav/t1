#4_2
import requests
import json


def currency_rates( val):
  url = 'https://www.cbr-xml-daily.ru/daily_json.js'
  val = val.upper()

  response = requests.get(url)
  dict_val = json.loads(response.text)
 #print(type(dict_val['Valute']['USD']['Value']))
  if val in dict_val['Valute']:
    return dict_val['Valute'][val]['Value']
  return None


print(currency_rates('EUR'))
print(currency_rates('usd'))