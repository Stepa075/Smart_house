import datetime
import time

designated_date = datetime.datetime.now()  # (2021, 1, 6, 15, 8, 24) # designated_date
designated_time = time.mktime(designated_date.timetuple())  # designated unix time in seconds

while True:
    time.sleep(1)  # 1 second delay
    current_time = int(time.time())  # every second get current unix time
    seconds = int(current_time - designated_time)  # calculation how much seconds left to desingated time
    "{:0>8}".format(str(datetime.timedelta(seconds=seconds)))

    seconds1 = seconds % 60
    minutes = (seconds / 60) % 60
    hours = (seconds / 3600) % 24
    days = (seconds / (60 * 60 * 24)) % 30
    month = (seconds / (60 * 60 * 24 * 30)) % 12
    Variables.time_for_program_start = ('%02d:%02d:%02d:%02d:%02d' % (month, days, hours, minutes, seconds1))
    print('%02d:%02d:%02d:%02d:%02d' % (month, days, hours, minutes, seconds1))