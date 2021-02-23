import time

# print(time.gmtime(0))
#
# # Local time
# print(time.localtime())
#
# # Number of seconds since start of epoch (1970)
# print(time.time())

# time.localtime() returns a named tuple (where fields within it can be accessed by name, as well as index)
# These print statements are printing redundant year, month and day (showing 2 different ways of accessing the values)
time_here = time.localtime()
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)
