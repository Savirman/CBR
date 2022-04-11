from urllib.request import urlopen
from xml.etree.ElementTree import parse
from datetime import date

current_date = date.today().strftime("%Y%m%d")
print(current_date)
current_day = current_date[6:9]
current_month = current_date[4:6]
current_year = current_date[0:4]
print(current_day)
print(current_month)
print(current_year)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
day = 1
while day <= int(current_day):
    fday = "{:>02}".format(day)
    str = "https://www.cbr.ru/scripts/XML_daily.asp?date_req={}/{}/{}".format(fday, current_month, current_year)
    print(str)
    var_url = urlopen(str)
    xmldoc = parse(var_url)

    for item in xmldoc.iter('ValCurs'):
        valkurs = item.attrib
        print(valkurs['Date'])

    for item in xmldoc.iterfind('Valute'):
        valuteid = item.attrib
        numcode = item.findtext('NumCode')
        charcode = item.findtext('CharCode')
        nominal = item.findtext('Nominal')
        name = item.findtext('Name')
        value = item.findtext('Value')

        print(valuteid['ID'])
        print(numcode)
        print(charcode)
        print(nominal)
        print(name)
        print(value)
    day = day + 1


