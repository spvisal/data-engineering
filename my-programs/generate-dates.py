from datetime import timedelta, date

start_date=date(2022,8,10)
end_date=date(2022,8,13)


print(range(int((end_date - start_date).days)))

def get_range(start_date,end_date):
    for n in range(int((end_date-start_date).days)):
        yield start_date+timedelta(n)

for single_date in get_range(start_date,end_date):
    print(single_date.strftime("%Y-%m-%d"))