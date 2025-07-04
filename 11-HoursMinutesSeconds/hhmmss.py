"""
Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The
argument for this parameter will be the number of seconds to be translated into the number of hours,
minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don’t show it: the
function should return '10m' rather than '0h 10m 0s'. The only exception is that
getHoursMinutesSeconds(0) should return '0s'
"""

def get_hour_minutes_seconds(total_seconds):
    hms = []
    remaining_seconds = total_seconds % 60
    remaining_minutes = (total_seconds // 60) % 60
    remaining_hours = total_seconds // 3600

    if remaining_hours > 0:
        hms.append(f"{remaining_hours}h")
    if remaining_minutes > 0:
        hms.append(f"{remaining_minutes}m")
    if remaining_seconds > 0 or len(hms) == 0:
        hms.append(f"{remaining_seconds}s")

    return " ".join(hms)

assert get_hour_minutes_seconds(30) == '30s'
assert get_hour_minutes_seconds(60) == '1m'
assert get_hour_minutes_seconds(90) == '1m 30s'
assert get_hour_minutes_seconds(3600) == '1h'
assert get_hour_minutes_seconds(3601) == '1h 1s'
assert get_hour_minutes_seconds(3661) == '1h 1m 1s'
assert get_hour_minutes_seconds(90042) == '25h 42s'
assert get_hour_minutes_seconds(0) == '0s'