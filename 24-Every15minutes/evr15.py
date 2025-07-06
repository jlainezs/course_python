"""
Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm.
Your solution should produce the following output:

12:00 am
12:15 am
12:30 am
12:45 am
1:00 am
1:15 am
--cut--
11:30 pm
11:45 pm

There are 96 lines in the full output.
"""

for meridian in ['am', 'pm']:
    for hour in [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        for minute in [0, 15, 30, 45]:
            print(f'{hour}:{minute:02d} {meridian}')