import datetime

def generate_dates(date_until="01/01/1938", count=29238):
    base = datetime.datetime.today()
    until = datetime.datetime.strptime(date_until, "%d/%m/%Y")
    days_between = (base-until).days

    date_list = [base - datetime.timedelta(days=x) for x in range(0, days_between)]

    with open('./dates.txt', 'w+') as dates_file:
        for date in date_list:
            dates_file.write(date.strftime('%m%d%Y') + '\n')
            dates_file.write(date.strftime('%d%m%Y') + '\n')
            dates_file.write(date.strftime('%Y%d%m') + '\n')
            dates_file.write(date.strftime('%Y%m%d') + '\n')
