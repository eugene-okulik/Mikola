import datetime

date_is_given = "Jan 15, 2023 - 12:05:33"

date_python = datetime.datetime.strptime(date_is_given, "%b %d, %Y - %H:%M:%S")
print(date_python)
print(date_python.strftime("%B"))
print(datetime.datetime.strftime(date_python, "%d.%m.%y, %H:%M"))
