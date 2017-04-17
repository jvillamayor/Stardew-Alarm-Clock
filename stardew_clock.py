'''
stardew_clock.py
Julius Villamayor, 2017
'''

import datetime
import os
import sys
import time


def check_args():
    if len(sys.argv) < 3:
        print('Usage: {} <hr> <min>'.format(sys.argv[0]))
        exit()
    if int(sys.argv[1]) > 23 or int(sys.argv[2]) > 59:
        print('Invalid time.')
        exit()


def print_pid():
    print('pid = ' + str(os.getpid()))


def print_alarm_time():
    time = get_inputted_time()
    time_of_day = 'AM'
    if time[0] >= 12:
        time[0] -= 12
        time_of_day = 'PM'
    print('Time set for {}:{} {}.'.format(time[0],
          str(time[1]).zfill(2), time_of_day))


def get_current_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    return [hour, minute]


def get_inputted_time():
    hour = int(sys.argv[1])
    minute = int(sys.argv[2])
    return [hour, minute]


if __name__ == '__main__':
    check_args()
    # print_pid()
    os.system("sudo osascript -e \"set Volume 3.5\"")
    os.system("open /Applications/Caffeine.app")
    print_alarm_time()
    time.sleep(3)
    os.system("pmset displaysleepnow")

    while(get_current_time() != get_inputted_time()):
        time.sleep(1)

    print("Launching Stardew Valley.")
    os.system("open /Applications/Stardew\ Valley.app")
