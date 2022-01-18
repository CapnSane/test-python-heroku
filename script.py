import time
from threading import Timer
import sched

# def function():
#     print("it's working!")

# t = Timer(5, function) ## This runs every 5 seconds the function "function"
# t.start() ## This part starts the t function


event_schedule = sched.scheduler(time.time, time.sleep)

def do_something():
    print("it's working!")
    event_schedule.enter(2, 1, do_something) ## It will repeat after 2 seconds itself

# event_schedule.enter(2, 1, do_something) ## Start running do_something() after 2 seconds
do_something()
event_schedule.run()
