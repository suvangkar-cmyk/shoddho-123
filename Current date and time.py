from datetime import date , time , datetime
today = date.today()
now = datetime.now()
print("Today's date is",today)
print("\nCurrnent date and time is",now)
print("\ndate components",today.year,today.month , today.day)