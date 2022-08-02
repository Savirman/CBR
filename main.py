#!/usr/bin/env python3
# by Dmitry Dolgov
# EPAM Diploma Project
# v.0.1 - 2022-04-12
# Data from the cbr.ru about valutes.
# Back-end of application
# Getting data

from urllib.request import urlopen
from xml.etree.ElementTree import parse
from datetime import date
import db

# Getting current date
current_date = date.today().strftime("%Y%m%d")       # Date type to string conversion (e.g. 2022-04-11 -> 20220411)
print(current_date)
current_day = current_date[6:9]                      # Selection the day from current date
current_month = current_date[4:6]                    # Selection the month from current date
current_year = current_date[0:4]                     # Selection the year from current date
print(current_day)
print(current_month)
print(current_year)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
'''
Organize a cycle to create a link for a query of valute data for day of the month from 1st to the current day.
Then take a portion of data from cbr.ru about valutes of every day of the current month.
'''
day = 1
while day <= int(current_day):
    fday = "{:>02}".format(day)
    str = "https://www.cbr.ru/scripts/XML_daily.asp?date_req={}/{}/{}".format(fday, current_month, current_year)
    print(str)
    var_url = urlopen(str)                            # Open url created earlier
    xmldoc = parse(var_url)                           # Parsing xml-file from the query

# Getting the date from xml. It's an attribute of ValCurs tag <ValCurs Date="02.03.2002" name="Foreign Currency Market">
    for item in xmldoc.iter('ValCurs'):
        valkurs = item.attrib
        #print(valkurs['Date'])

    '''
    Getting the data about valutes.
    All the required data about a valute is in the <Valute></Valute> block.
    We find the data in this block and assign it to the appropriate vars
    '''

    for item in xmldoc.iterfind('Valute'):
        valuteid = item.attrib                  # Valute ID is an attribute of Valute tag, e.g. <Valute ID="R01010">
        numcode = item.findtext('NumCode')
        charcode = item.findtext('CharCode')
        nominal = item.findtext('Nominal')
        name = item.findtext('Name')
        value = item.findtext('Value')

        print(valkurs['Date'])
        print(valuteid['ID'])
        print(numcode)
        print(charcode)
        print(nominal)
        print(name)
        print(value)
        print(" ")

        # Indertion tre data about valutes into table "valutes" of DB cbr
        insert_values_into_valutes = f"INSERT INTO valutes (date, valuteid, numcode, charcode, nominal, name, value) VALUES ('{valkurs['Date']}', '{valuteid['ID']}', {numcode},'{charcode}', {nominal}, '{name}', '{value}')"
        db.insertion(db.connection, insert_values_into_valutes)

    day = day + 1

db.connection.close()