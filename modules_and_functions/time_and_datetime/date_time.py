# import time
#
# print("Epoch starts at: " + time.strftime('%c', time.gmtime(0)))
# print(f"Current time zone: {time.tzname[0]}\n\tOffset: {time.timezone}")
#
# if time.daylight != 0:
#     print("\nDAYLIGHT SAVINGS TIME IS CURRENTLY IN EFFECT")
#     print("The DST timezone is " + time.tzname[1])
#
# local_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
# print(f"Local time is: {local_time}")

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
