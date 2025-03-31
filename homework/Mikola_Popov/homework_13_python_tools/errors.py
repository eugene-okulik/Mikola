import datetime

now_date = datetime.datetime.now()
print(now_date)
today_midnight = datetime.datetime.now().replace(
    hour=0, minute=0, second=0, microsecond=0
)
print(now_date - today_midnight)
new_time = now_date - today_midnight
print(new_time + datetime.timedelta(hours=10))
