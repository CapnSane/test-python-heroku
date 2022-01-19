import os
from datetime import *
import time
import random
from threading import Timer
import sched

limit_num = 9

# def function():
#     print("it's working!")

# t = Timer(5, function) ## This runs every 5 seconds the function "function"
# t.start() ## This part starts the t function

with open('date.txt') as f:
    lines = f.readlines()[0]

timestamp = time.time()
t0 = datetime.fromtimestamp(timestamp)
today = t0.strftime("%m/%d/%Y - %H:%M")

def save_date(i):
    t = datetime.fromtimestamp(timestamp - i*100)
    formatT = t.strftime("%m/%d/%Y - %H:%M")
    os.system(f'echo -n {formatT} > date.txt')

# event_schedule = sched.scheduler(time.time, time.sleep)

# def do_something():
#     print("it's working!")
#     event_schedule.enter(2, 1, do_something) ## It will repeat after 2 seconds itself

# event_schedule.enter(2, 1, do_something) ## Start running do_something() after 2 seconds
# # do_something()
# event_schedule.run()

def main():
    if (today[0:10] != lines[0:10]):
            for i in reversed(range(random.randint(1, limit_num))):
                save_date(i)
                print(lines[0:10])
    else:
        print('it is different')

main()