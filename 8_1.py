#8_1
import re
RE_UN = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+'
RE2_DM = r'[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
RE_DATE_PATTERN = re.compile(RE_UN + r'@' + RE2_DM)


def email_parse( email):
  dict_email = {}
  assert RE_DATE_PATTERN.match(email), f'wrong email {email}'

  dict_email['username'] = email[:email.find('@')]
  dict_email['domain'] = email[email.find('@')+1:]
  print(dict_email)


def email_parse1( email):
  dict_email = {}
  assert RE_DATE_PATTERN.match(email), f'wrong email {email}'

  dict_email['username'] = re.search(RE_UN+r'@', email).group(0)[:-1]
  dict_email['domain'] = re.search(r'@'+RE2_DM, email).group(0)[1:]
  print(dict_email)
  

email_parse('qwe1@mail.ru')
email_parse1('qwe1@mail.ru')