import datetime
print(datetime.datetime.now())

print(datetime.datetime.utcnow())

print(datetime.date.today())

random_date = datetime.date.fromtimestamp(12345678)
print(type(random_date))
print(random_date.month)
print(random_date.year)
print(random_date.day)