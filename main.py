from urllib.request import urlopen
from xml.etree.ElementTree import parse

var_url = urlopen('https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002')
xmldoc = parse(var_url)

for item in xmldoc.iterfind('Valute'):
    numcode = item.findtext('NumCode')
    charcode = item.findtext('CharCode')
    nominal = item.findtext('Nominal')
    name = item.findtext('Name')
    value = item.findtext('Value')


    print(numcode)
    print(charcode)
    print(nominal)
    print(name)
    print(value)
