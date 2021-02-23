import time
# from time import time as my_timer
from time import perf_counter as my_timer
import random

input("Press 'ENTER' to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)

start_time = my_timer()

input("Press 'ENTER' to stop")
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print(f"Your reaction time: {end_time-start_time}")
