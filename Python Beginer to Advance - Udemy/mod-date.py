import datetime as dt

print('Hari ini', dt.datetime.now())
print('Tanggal', dt.date(2025, 2, 1))

mytime = dt.datetime.now()
print(mytime.strftime('%A'))