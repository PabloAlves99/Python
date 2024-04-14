def make_readable(seconds):
    return f'{seconds//3600:02}:{seconds//60%60:02}:{seconds%60:02}'

# def make_readable(seconds):
#     seconds_per_hour = 3600
#     seconds_per_minute = 60

#     hours = seconds // seconds_per_hour

#     rest_hours = seconds % seconds_per_hour
#     minutes = rest_hours // seconds_per_minute

#     end_seconds = seconds % seconds_per_minute

#     return '{:02}:{:02}:{:02}'.format(hours, minutes, end_seconds)

# make_readable = lambda seconds:f'{seconds//3600:02}:{seconds//60%60:02}:{seconds%60:02}' # noqa


if __name__ == '__main__':
    print(make_readable(0))
    print(make_readable(59))
    print(make_readable(60))
    print(make_readable(3599))
    print(make_readable(3600))
    print(make_readable(86399))
    print(make_readable(86400))
    print(make_readable(359999))
