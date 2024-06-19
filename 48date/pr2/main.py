from datetime import datetime

datetime1 = datetime(2222, 12, 10, 18, 10, 45)

print(datetime1.strftime('%d-%b-%Y'))  # 10-Dec-2222
print(datetime1.strftime('%d-%m-%Y'))  # 10-12-2222
print(datetime1.strftime('%d-%B-%Y'))  # 10-December-2222
print(datetime1.strftime('%D-%b-%Y'))  # 12/10/22-Dec-2222
print(datetime1.strftime('%d/%m/%Y'))  # 10/12/2222
print(datetime1.strftime('%d-%b-%Y %H:%M:%S'))  # 10-Dec-2222 18:10:45

date1 = '10/12/2222'
converted_date = datetime.strptime(date1, '%d/%m/%Y')
print(converted_date)
