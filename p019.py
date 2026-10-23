from datetime import date, timedelta

def daterange(start_date, end_date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)

start = date(1901, 1, 1)
end = date(2000, 12, 31)

mask = [day.strftime("%a") == "Sun" and day.strftime("%d") == "01" for day in daterange(start, end)]

print(sum(mask))