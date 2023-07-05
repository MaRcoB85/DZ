from datetime import datetime, timedelta


start_date = datetime(2023, 3, 27, 19, 15)
dates = [start_date]

for i in range(1, 32):
    if i % 2 == 0:
        next_date = dates[-1] + timedelta(days=4)
    else:
        next_date = dates[-1] + timedelta(days=3)
    dates.append(next_date)

for i, date in enumerate(dates):
    print(f"Lecture {i+1:2}: {date.strftime('%d %b %Y %H:%M')}")
