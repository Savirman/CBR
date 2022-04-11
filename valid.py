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
    day = day + 1





